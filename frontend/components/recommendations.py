from typing import Any, Dict

import streamlit as st


def display_recommendations(analysis: Dict[str, Any]) -> None:
    suggestions = analysis.get("suggestions") or []
    if not suggestions:
        return

    st.markdown("### 💡 Recommendations")
    for suggestion in suggestions:
        st.markdown(f"- {suggestion}")
