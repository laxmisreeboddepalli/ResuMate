# modules/cover_letter.py

import streamlit as st

def render_cover_letter():
    st.subheader("📝 Cover Letter Generator")

    parsed_data = st.session_state.get("parsed_resume_data", {})
    role = st.session_state.get("selected_role", "")
    
    if not parsed_data or not role:
        st.warning("⚠️ Please upload a resume and select a job role first.")
        return

    name = parsed_data.get("name", "Your Name")
    email = parsed_data.get("email", "your.email@example.com")
    resume_summary = parsed_data.get("raw_text", "")[:1000]  # Use first 1000 characters

    company = st.text_input("🏢 Company Name (optional)")
    user_intro = st.text_area("📄 Add a short personal introduction (optional)", placeholder="E.g., Passionate about building scalable systems...")

    if st.button("✍️ Generate Cover Letter"):
        with st.spinner("Generating..."):

            letter = f"""
Dear Hiring Manager{f" at {company}" if company else ""},

I am writing to express my interest in the {role} position{f" at {company}" if company else ""}. With a strong foundation in my field and a passion for growth, I believe I would be a valuable addition to your team.

{user_intro if user_intro else "Throughout my academic and project experience, I’ve honed practical skills and a strong problem-solving mindset."}

From my resume:
{resume_summary.strip()}

I am particularly excited about this opportunity because it aligns well with my career goals and interests. I would welcome the chance to discuss how my skills and experience could benefit your organization.

Thank you for considering my application. I look forward to the possibility of contributing to your team.


Sincerely,  
{name}  
📧 {email}
"""

            st.success("✅ Cover letter generated!")
            st.text_area("📄 Your Cover Letter", letter.strip(), height=350)
            st.download_button("⬇️ Download Cover Letter", letter.strip(), file_name="cover_letter.txt")

    if st.button("🔙 Back to Dashboard"):
        st.session_state.selected_module = None
        st.rerun()
