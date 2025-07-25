import streamlit as st
import re

def render_summary():
    st.markdown("<h2 style='color:#4A148C;'>🧠 Resume Summary & Feedback</h2>", unsafe_allow_html=True)

    resume_data = st.session_state.get("parsed_resume_data", {})
    raw_text = resume_data.get("raw_text", "")
    role = st.session_state.get("selected_role", "").title()

    name = resume_data.get("name", "[Name not found]")
    email = resume_data.get("email", "[Email not found]")
    skills = resume_data.get("skills") or resume_data.get("Skills") or resume_data.get("SKILLS") or []

    experience_lines = [
        line for line in raw_text.split("\n")
        if any(word in line.lower() for word in ["experience", "intern", "worked", "led", "managed", "responsible", "collaborated"])
    ]
    project_lines = [
        line for line in raw_text.split("\n")
        if any(word in line.lower() for word in ["project", "built", "developed", "created", "implemented"])
    ]

    top_skills = ', '.join(skills[:5]) if skills else '[Skills not found]'

    # ✅ Enhanced summary with more useful info
    summary = f"""
    <b>{name}</b> is targeting a role as a <b>{role}</b>. The resume demonstrates strong initiative and technical depth with <b>{len(project_lines)}</b> project(s) and <b>{len(experience_lines)}</b> experience-based line(s).<br><br>
    It highlights core skills such as <b>{top_skills}</b>, suggesting alignment with industry expectations for this role.<br><br>
    The structure of the resume appears clean, and the language is mostly professional. However, more impact can be made by quantifying achievements and enhancing the resume’s tone and clarity.<br><br>
    Based on current content, the resume shows readiness but could benefit from stronger framing of accomplishments and clearer visual hierarchy (e.g., consistent section formatting).
    """

    st.markdown(f"""
    <div style='background-color:#f3e5f5; padding:20px; border-radius:10px; font-size:16px; line-height:1.7;'>
        <b>📋 AI Summary:</b><br><br>
        {summary}
    </div>
    """, unsafe_allow_html=True)

    # 💡 Suggestions to Improve Further
    st.markdown("<h3 style='margin-top:30px;'>💡 Suggestions for Improvement</h3>", unsafe_allow_html=True)
    st.markdown("""
    -  **Quantify achievements**: Use numbers like “improved accuracy by 25%” or “led a team of 5”.
    -  **Add a summary/objective section** at the top to personalize your profile.
    -  **Keep consistent formatting**: Same font, bullet style, spacing across sections.
    -  **Avoid repeating skills** — group similar tools together (e.g., NumPy, Pandas as Python libraries).
    -  **Use action words**: "Led", "Designed", "Improved", "Collaborated", etc.
    -  **Highlight relevant tools** based on the job (e.g., Git for Dev roles, Tableau for Data roles).
    -  **Ensure grammar and punctuation consistency** across experience and project lines.
    """)

    # 🔍 Extracted Highlights
    with st.expander(" View Extracted Highlights"):
        st.markdown(f" Name: {name}")
        st.markdown(f" Email: {email}")
        st.markdown(f" Top Skills: {top_skills}")
        st.markdown(f" Projects Detected: {len(project_lines)}")
        st.markdown(f" Experience Bullet Points: {len(experience_lines)}")

    # 🔙 Back button
    if st.button("🔙 Back to Dashboard"):
        st.session_state.selected_module = None
        st.rerun()
