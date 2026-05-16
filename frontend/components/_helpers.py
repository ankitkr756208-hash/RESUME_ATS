from typing import Tuple


def get_score_color(score: float) -> Tuple[str, str]:
    """Return (text_color, background_color) for a 0–100 score."""
    if score >= 80:
        return "#2e7d32", "#e8f5e9"  # green
    if score >= 60:
        return "#f57c00", "#fff3e0"  # orange
    return "#c62828", "#ffebee"      # red


def get_score_emoji(score: float) -> str:
    """Emoji that matches the score band — used in headlines."""
    if score >= 90:
        return "🌟"
    if score >= 80:
        return "✅"
    if score >= 70:
        return "👍"
    if score >= 60:
        return "⚠️"
    return "🔴"


def get_severity_style(severity: str) -> Tuple[str, str, str]:
    """
    Return (icon, text_color, background_color) for an IssueDetail severity.
    Matches the values the backend emits in `detailed_feedback[].severity_level`.
    """
    level = (severity or "").lower()
    if level in ("critical", "high"):
        return "🔴", "#c62828", "#ffebee"
    if level == "medium":
        return "🟡", "#f57c00", "#fff3e0"
    return "🟢", "#2e7d32", "#e8f5e9"
