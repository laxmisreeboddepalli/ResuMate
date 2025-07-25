# utils/resume_uploader.py

import streamlit as st
import os
from utils.resume_parser import parse_resume

def resume_uploader_ui():
    st.markdown(
        """
        <div style='
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(10px);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            margin-bottom: 30px;
        '>
            <h2 style='text-align:center; color: #004080;'>Upload Your Resume</h2>
        """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Choose a PDF or DOCX resume", type=["pdf", "docx"])

    if uploaded_file is not None:
        file_path = os.path.join("temp", uploaded_file.name)
        os.makedirs("temp", exist_ok=True)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.success("✅ Resume uploaded successfully!")

        # Store both resume path and bytes in session
        st.session_state.resume_path = file_path
        st.session_state.resume_bytes = uploaded_file.getvalue()

        # Parse resume using path
        parsed_data = parse_resume(file_path)
        st.session_state.parsed_resume_data = parsed_data  # ← Make available to all modules

        name = parsed_data.get('name', 'N/A')
        email = parsed_data.get('email', 'N/A')
        raw_text = parsed_data.get('raw_text', '')

        # Display extracted info
        email_display = f"<a href='mailto:{email}' style='color:#1976d2;'>{email}</a>" if email != "N/A" else "N/A"
        st.markdown(f"""
        <h3 style='color: #004080;'>📄 Extracted Basic Information</h3>
        <div style='line-height: 1.8; font-size: 16px;'>
            <b>👤 Name:</b> {name}<br>
            <b>📧 Email:</b> {email_display}
        </div>
        """, unsafe_allow_html=True)

        with st.expander("📄 View Full Resume Text", expanded=False):
            st.markdown(
                f"<div style='color:#004080; font-size:15px; white-space: pre-wrap;'>{raw_text}</div>",
                unsafe_allow_html=True
            )

        st.markdown("</div>", unsafe_allow_html=True)
        return raw_text

    st.markdown("</div>", unsafe_allow_html=True)
    return None
