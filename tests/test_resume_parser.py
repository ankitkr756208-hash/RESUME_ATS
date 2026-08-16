from pathlib import Path

import pytest

from backend.services import pdf_export
from backend.services.resume_parser import validate_file


PDF_BYTES = b"%PDF-1.4\n1 0 obj\n<<>>\nendobj\ntrailer\n<<>>\n%%EOF"
DOCX_BYTES = b"PK\x03\x04" + b"x" * 100


def test_validate_file_accepts_pdf_without_magic_dependency():
    is_valid, error_msg, file_type = validate_file(PDF_BYTES, "resume.pdf")

    assert is_valid is True
    assert error_msg == ""
    assert file_type == "pdf"


def test_validate_file_rejects_unknown_binary_file():
    is_valid, error_msg, file_type = validate_file(b"not a real resume", "resume.txt")

    assert is_valid is False
    assert file_type is None
    assert "Unsupported file type" in error_msg or "Could not identify" in error_msg


def test_validate_file_accepts_docx_zip_signature():
    is_valid, error_msg, file_type = validate_file(DOCX_BYTES, "resume.docx")

    assert is_valid is True
    assert file_type == "docx"


@pytest.mark.asyncio
async def test_generate_combined_pdf_uses_sync_playwright_fallback(monkeypatch):
    monkeypatch.setattr(pdf_export, "WEASYPRINT_INSTALLED", False)
    monkeypatch.setattr(pdf_export, "PLAYWRIGHT_INSTALLED", True)
    monkeypatch.setattr(pdf_export, "REPORTLAB_INSTALLED", True)
    monkeypatch.setattr(pdf_export, "async_playwright", None)

    class FakePage:
        def set_content(self, *args, **kwargs):
            return None

        def pdf(self, *args, **kwargs):
            return b"%PDF-1.4\nfake pdf\n%%EOF"

    class FakeBrowser:
        def new_page(self):
            return FakePage()

        def close(self):
            return None

    class FakePlaywright:
        chromium = type("Chromium", (), {"launch": staticmethod(lambda headless=True: FakeBrowser())})

    class FakeSyncPlaywright:
        def __enter__(self):
            return FakePlaywright()

        def __exit__(self, exc_type, exc, tb):
            return False

    monkeypatch.setattr(pdf_export, "sync_playwright", lambda: FakeSyncPlaywright())

    pdf_bytes = await pdf_export.generate_combined_pdf({"Summary": "<h1>Hello</h1>"})

    assert pdf_bytes.startswith(b"%PDF")
