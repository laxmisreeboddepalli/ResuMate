import streamlit as st
import re

def render_projects_experience_review():
    st.markdown("<h2 style='color:#D84315;'>📄 Summary</h2>", unsafe_allow_html=True)

    resume_text = st.session_state.get("parsed_resume_data", {}).get("raw_text", "")
    role = st.session_state.get("selected_role", "").lower()

    project_keywords = ["project", "built", "developed", "designed", "created", "implemented"]
    experience_keywords = ["experience", "intern", "worked", "contributed", "developed", "led", "responsible"]

    project_lines = [line for line in resume_text.split("\n") if any(k in line.lower() for k in project_keywords)]
    experience_lines = [line for line in resume_text.split("\n") if any(k in line.lower() for k in experience_keywords)]

    # Summary box
    st.markdown(f"""
        <div style="background-color:#e6f4ea; padding:20px; border-radius:10px; font-size:16px;">
        Based on your resume, we detected <b>{len(project_lines)}</b> project lines and <b>{len(experience_lines)}</b> experience lines.
        <br><br>
        Make sure each item reflects your contribution clearly and connects to the <b>{role.title()}</b> role.
        Consider rewriting vague sentences and focus on your <b>impact</b>, <b>technologies used</b>, and <b>results achieved</b>.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📌 Detected Project-Related Lines")
    if project_lines:
        for line in project_lines:
            st.markdown(f"- {line.strip()}")
    else:
        st.info("No major projects detected.")

    st.markdown("### 🧳 Detected Experience-Related Lines")
    if experience_lines:
        for line in experience_lines:
            st.markdown(f"- {line.strip()}")
    else:
        st.info("No experience content found.")

    st.markdown("### ✅ Suggestions to Improve")
    st.markdown("""
    **Projects:**
    - Use bullet points with strong action verbs (e.g., Built, Led, Integrated).
    - Highlight results: metrics, impact, tools used.
    - Keep only relevant projects for the selected role.

    **Experience:**
    - Emphasize leadership, ownership, and outcomes.
    - Remove outdated or unrelated experience.
    - Use consistent formatting with job title, company, and timeline.
    """)

    st.markdown("### 📝 Summary")
    summary = f"""
Based on your resume, we detected {len(project_lines)} project lines and {len(experience_lines)} experience lines.

Make sure each item reflects your contribution clearly and connects to the **{role}** role. 
Consider rewriting vague sentences and focus on your **impact**, **technologies used**, and **results achieved**.
"""
    st.success(summary.strip())

    if st.button("🔙 Back to Dashboard"):
        st.session_state["selected_module"] = None
        st.rerun()
