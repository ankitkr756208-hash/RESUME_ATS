from typing import Any, Dict

import streamlit as st

from frontend.components._helpers import get_score_color, get_score_emoji


# Component max scores match backend/core/config.py SCORE_WEIGHTS.
# (Backend returns each component's score on its own scale, not 0–100.)
COMPONENTS = [
    ("Formatting",        "formatting",        20, "📝"),
    ("Keywords & Skills", "keywords",          25, "🔑"),
    ("Content Quality",   "content",           25, "📄"),
    ("Skill Validation",  "skill_validation",  15, "✅"),
    ("ATS Compatibility", "ats_compatibility", 15, "🤖"),
]


def display_overall_score(analysis: Dict[str, Any]) -> None:
    """Big colored score card with a short interpretation line."""
    score = float(analysis.get("ATS_score", analysis.get("ats_score", 0)))
    interpretation = analysis.get("interpretation", "")
    text_color, bg_color = get_score_color(score)
    emoji = get_score_emoji(score)

    st.markdown("## 📊 Analysis Results")
    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        st.markdown(
            f"""
            <div style="text-align:center; padding:2rem; background-color:{bg_color};
                        border-radius:15px; box-shadow:0 4px 6px rgba(0,0,0,0.1);">
                <h1 style="color:{text_color}; font-size:4.5rem; margin:0; font-weight:bold;">
                    {emoji} {score:.0f}
                </h1>
                <h3 style="color:{text_color}; margin:0.5rem 0;">Overall ATS Score</h3>
                <p style="color:#666; margin-top:0.5rem;">{interpretation}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


def display_score_breakdown(analysis: Dict[str, Any]) -> None:
    """Five progress bars, one per scoring component."""
    component_scores = analysis.get("component_scores") or {}
    st.markdown("### 📈 Score Breakdown")

    left, right = st.columns(2)
    for i, (label, key, max_score, icon) in enumerate(COMPONENTS):
        value = float(component_scores.get(key, 0))
        percentage = value / max_score if max_score else 0
        bar_color = "green" if percentage >= 0.8 else "orange" if percentage >= 0.6 else "red"

        with left if i % 2 == 0 else right:
            st.markdown(f"**{icon} {label}**")
            st.markdown(
                f"""
                <div style="background-color:#e0e0e0; border-radius:10px; height:20px; margin-bottom:5px;">
                    <div style="background-color:{bar_color}; width:{percentage * 100}%;
                                height:100%; border-radius:10px; transition:width 0.5s;"></div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.markdown(f"**{value:.0f}/{max_score}**")
            st.markdown("")
