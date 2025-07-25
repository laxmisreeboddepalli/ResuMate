import streamlit as st


def render_job_readiness_analyzer():
    st.markdown("""
        <h2 style='color:#4A148C;'>✅ Job Readiness Analyzer</h2>
        <h4 style='margin-top:0; color:gray;'>❓ \"Am I Ready to Apply?\" – Score & actionable checklist</h4>
    """, unsafe_allow_html=True)

    resume_data = st.session_state.get("parsed_resume_data", {})
    role = st.session_state.get("selected_role", "").title()
    name = resume_data.get("name", "[Name not found]")
    email = resume_data.get("email", "[Email not found]")
    phone = resume_data.get("phone", "[Phone not found]")
    skills = resume_data.get("skills") or resume_data.get("Skills") or resume_data.get("SKILLS") or []
    raw_text = resume_data.get("raw_text", "")

    # Analyze based on job role matching
    job_keywords = role.lower().split()
    matched_skills = [s for s in skills if any(k in s.lower() for k in job_keywords)]

    project_lines = [line for line in raw_text.split("\n") if any(word in line.lower() for word in ["project", "built", "developed"])]
    experience_lines = [line for line in raw_text.split("\n") if any(word in line.lower() for word in ["experience", "intern", "worked", "led"])]

    # Scoring logic
    score = 50
    score += min(len(matched_skills) * 5, 25)  # Up to 25 points for relevant skills
    score += min(len(project_lines) * 5, 15)    # Up to 15 points for projects
    score += min(len(experience_lines) * 2, 10) # Up to 10 points for experience

    st.markdown(f"""
    <div style='background-color:#e8f5e9; padding:20px; border-radius:10px;'>
        <h3 style='color:#2e7d32;'>🧮 Job Readiness Score: {score} / 100</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h4 style='margin-top:30px;'>🚧 Recommendations</h4>
    <ul>
    """, unsafe_allow_html=True)

    if len(matched_skills) < 3:
        st.markdown("- Add more job-specific technical skills.")
    if len(project_lines) < 2:
        st.markdown("- Highlight at least 2 relevant projects.")
    if len(experience_lines) < 2:
        st.markdown("- Add or elaborate on past internships or work experience.")
    st.markdown("</ul>", unsafe_allow_html=True)

    with st.expander("📄 Details Checked"):
        st.markdown(f"**Name Found:** {name}")
        st.markdown(f"**Email:** {email}")
        st.markdown(f"**Phone:** {phone}")
        st.markdown(f"**Skills Found:** {', '.join(skills) if skills else '[Not Found]'}")
        st.markdown(f"**Experience Lines:** {len(experience_lines)}")
        st.markdown(f"**Project Lines:** {len(project_lines)}")

    if st.button("🔙 Back to Dashboard"):
        st.session_state.selected_module = None
        st.rerun()
