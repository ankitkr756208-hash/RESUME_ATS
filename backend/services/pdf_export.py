import asyncio
import html as html_lib
import io
import logging
from html.parser import HTMLParser

WEASYPRINT_IMPORT_ERROR = None
PLAYWRIGHT_IMPORT_ERROR = None
REPORTLAB_IMPORT_ERROR = None

try:
    from weasyprint import HTML, CSS
    WEASYPRINT_INSTALLED = True
except Exception as exc:  # WeasyPrint may fail to import because native system libs are missing
    WEASYPRINT_INSTALLED = False
    WEASYPRINT_IMPORT_ERROR = exc
    HTML = None
    CSS = None

try:
    from playwright.async_api import async_playwright
    PLAYWRIGHT_INSTALLED = True
except Exception as exc:  # Browser-based fallback if native GTK libs are unavailable
    PLAYWRIGHT_INSTALLED = False
    PLAYWRIGHT_IMPORT_ERROR = exc
    async_playwright = None

try:
    from playwright.sync_api import sync_playwright
except Exception as exc:  # sync caller is safer in async web servers on Windows
    sync_playwright = None
    if not PLAYWRIGHT_INSTALLED:
        PLAYWRIGHT_IMPORT_ERROR = exc

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, PageBreak
    REPORTLAB_INSTALLED = True
except Exception as exc:
    REPORTLAB_INSTALLED = False
    REPORTLAB_IMPORT_ERROR = exc
    letter = None
    getSampleStyleSheet = None
    Paragraph = None
    SimpleDocTemplate = None
    Spacer = None
    PageBreak = None

logger = logging.getLogger('ats_resume_scorer')


class _HTMLTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self._parts: list[str] = []

    def handle_data(self, data: str) -> None:
        if not data:
            return
        text = data.strip()
        if text:
            self._parts.append(text)

    def get_text(self) -> str:
        return '\n'.join(self._parts)


def _html_to_text(html_text: str) -> str:
    parser = _HTMLTextExtractor()
    parser.feed(html_text or '')
    parser.close()
    text = parser.get_text()
    return '\n'.join(line.strip() for line in text.splitlines() if line.strip())


def _generate_reportlab_pdf(html_docs: dict[str, str]) -> bytes:
    if not REPORTLAB_INSTALLED:
        raise RuntimeError(
            'PDF export is unavailable because neither WeasyPrint nor the pure-Python fallback is installed. '
            f'ReportLab import error: {REPORTLAB_IMPORT_ERROR}'
        )

    buffer = io.BytesIO()
    styles = getSampleStyleSheet()
    story = []

    for index, (name, html_str) in enumerate(html_docs.items()):
        if index:
            story.append(PageBreak())

        title = (name or 'Report').replace('_', ' ').replace('-', ' ').title()
        story.append(Paragraph(title, styles['Title']))
        story.append(Spacer(1, 12))

        text = _html_to_text(html_str)
        if not text:
            text = 'No report content available.'

        for line in text.splitlines()[:200]:
            if line.strip():
                story.append(Paragraph(line.strip(), styles['BodyText']))

        story.append(Spacer(1, 12))

    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36,
    )
    doc.build(story)
    return buffer.getvalue()


def _looks_like_html(value: str | None) -> bool:
    if not value:
        return False
    lowered = value.lower()
    tag_markers = ('<html', '<body', '<style', '<div', '<table', '<p', '<section', '<h1', '<h2', '<span')
    return any(marker in lowered for marker in tag_markers)


def _combine_html_docs(html_docs: dict[str, str]) -> str:
    sections: list[str] = []
    for name, html_str in html_docs.items():
        cleaned = (html_str or '').strip()
        if not cleaned:
            continue
        title = html_lib.escape((name or 'Report').replace('_', ' ').title())
        sections.append(
            f"<section style='margin-bottom: 28px; page-break-inside: avoid;'>"
            f"<h2 style='margin: 0 0 12px; font-size: 18px; color: #111827;'>{title}</h2>"
            f"{cleaned}</section>"
        )

    if not sections:
        raise ValueError('No HTML content was provided for PDF export.')

    return (
        "<!DOCTYPE html>"
        "<html><head><meta charset='utf-8' />"
        "<style>"
        "body { font-family: Arial, sans-serif; margin: 24px; color: #111827; background: #ffffff; }"
        "h1, h2, h3 { color: #111827; }"
        "table { border-collapse: collapse; width: 100%; }"
        "th, td { border: 1px solid #d1d5db; padding: 8px; text-align: left; }"
        "p { margin: 8px 0; }"
        "section { margin-bottom: 20px; }"
        "</style></head><body>"
        f"{''.join(sections)}"
        "</body></html>"
    )


def _generate_playwright_pdf_sync(html_docs: dict[str, str]) -> bytes:
    if not PLAYWRIGHT_INSTALLED or sync_playwright is None:
        raise RuntimeError(
            'PDF export is unavailable because neither WeasyPrint nor Playwright is installed. '
            f'WeasyPrint import error: {WEASYPRINT_IMPORT_ERROR}; Playwright import error: {PLAYWRIGHT_IMPORT_ERROR}'
        )

    combined_html = _combine_html_docs(html_docs)
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(combined_html, wait_until='networkidle')
        pdf_bytes = page.pdf(print_background=True, prefer_css_page_size=True, format='A4')
        browser.close()
    return pdf_bytes


async def _generate_playwright_pdf(html_docs: dict[str, str]) -> bytes:
    return await asyncio.to_thread(_generate_playwright_pdf_sync, html_docs)


async def generate_combined_pdf(html_docs: dict[str, str]) -> bytes:
    if not html_docs:
        raise ValueError('No HTML content was provided for PDF export.')

    if WEASYPRINT_INSTALLED:
        documents = []

        # Render all HTML strings to WeasyPrint Document objects.
        for name, html_str in html_docs.items():
            if not _looks_like_html(html_str):
                raise ValueError(
                    f"The PDF report for '{name}' does not contain HTML/CSS content. "
                    'A styled PDF requires valid HTML markup, not plain text.'
                )
            doc = HTML(string=html_str).render()
            documents.append(doc)

        # Merge them into the first document
        first_doc = documents[0]
        for other_doc in documents[1:]:
            for page in other_doc.pages:
                first_doc.pages.append(page)

        # Write combined PDF bytes
        return first_doc.write_pdf()

    if PLAYWRIGHT_INSTALLED:
        logger.warning(
            'WeasyPrint could not load its native libraries; using Playwright HTML-to-PDF fallback. '
            f'Underlying error: {WEASYPRINT_IMPORT_ERROR}'
        )
        try:
            return await _generate_playwright_pdf(html_docs)
        except Exception as exc:
            logger.warning(
                'Playwright PDF fallback failed; falling back to ReportLab text export. '
                f'Underlying error: {exc}'
            )

    html_sections = [value for value in html_docs.values() if _looks_like_html(value)]
    if html_sections:
        raise RuntimeError(
            'HTML/CSS PDF export is unavailable because neither WeasyPrint nor Playwright is installed. '
            'WeasyPrint could not import due to missing native GTK/GLib libraries, and Playwright is not available. '
            'Install the required Windows libraries or install Playwright to render the HTML as a styled PDF.'
        )

    logger.warning(
        'WeasyPrint and Playwright are unavailable; using pure-Python ReportLab fallback for plain-text export. '
        f'Underlying error: {WEASYPRINT_IMPORT_ERROR}'
    )
    return _generate_reportlab_pdf(html_docs)
