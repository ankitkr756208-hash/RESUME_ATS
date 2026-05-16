from typing import Any, Dict

import streamlit as st


def display_skill_validation(analysis: Dict[str, Any]) -> None:
    details = analysis.get("skill_validation_details") or {}
    validated = details.get("validated", [])
    unvalidated = details.get("unvalidated", [])
    total = details.get("total", len(validated) + len(unvalidated))
    pct = details.get("validation_pct", 0.0)

    st.markdown("### ✅ Skill Validation")

    if total == 0:
        st.info("No skills detected on the resume.")
        return

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Skills", total)
    c2.metric("Validated", len(validated))
    c3.metric("Validation %", f"{pct:.0f}%")

    st.progress(min(max(pct / 100.0, 0.0), 1.0))

    if validated:
        with st.expander(f"✅ Validated skills ({len(validated)})", expanded=False):
            for entry in validated:
                skill = entry.get("skill", "?")
                projects = entry.get("projects", []) or []
                similarity = entry.get("similarity")

                project_text = ", ".join(projects[:3]) if projects else "experience section"
                sim_text = f" ({similarity * 100:.0f}% match)" if isinstance(similarity, (int, float)) else ""
                st.markdown(f"- **{skill}**{sim_text} — demonstrated in: {project_text}")

    if unvalidated:
        with st.expander(f"⚠️ Unvalidated skills ({len(unvalidated)})", expanded=False):
            st.caption("These skills are listed but not tied to a project or experience bullet.")
            for skill in unvalidated:
                st.markdown(f"- ❌ {skill}")
