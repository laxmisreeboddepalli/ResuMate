import streamlit as st
import re

def render_ats_checker():
    st.markdown("## 📄 ATS Compatibility Checker")
    st.markdown("This module checks if your resume is likely to pass through Applicant Tracking Systems (ATS).")

    resume_text = st.session_state.get("parsed_resume_data", {}).get("raw_text", "")
    resume_path = st.session_state.get("resume_path", "")

    if not resume_text:
        st.warning("⚠️ Please upload and parse a resume first.")
        return

    # Initialize score and issues
    score = 100
    issues = []

    # 1. Check for images (based on raw text, not foolproof but gives indication)
    if "image" in resume_text.lower():
        score -= 10
        issues.append("❌ Avoid using images/logos — ATS can’t parse visuals.")

    # 2. Check for tables (look for words often present in tables or multiple tabs/spaces)
    if re.search(r"\t|\s{4,}", resume_text):
        score -= 10
        issues.append("❌ Avoid using tables — ATS may skip or misread them.")

    # 3. Check for fancy bullet symbols
    fancy_bullets = ["★", "❄", "●", "◆", "✓"]
    if any(b in resume_text for b in fancy_bullets):
        score -= 10
        issues.append("❌ Use standard bullet points — avoid fancy symbols like ★ or ❄.")

    # 4. Check for uncommon fonts (approximate — not possible via raw text, so we skip)

    # 5. Check for section headers
    required_sections = ["education", "experience", "skills"]
    missing_sections = [s for s in required_sections if s not in resume_text.lower()]
    if missing_sections:
        score -= 10 * len(missing_sections)
        issues.append(f"❌ Missing sections: {', '.join(missing_sections).title()}.")

    # Display Score
    st.subheader("🧮 ATS Score")
    st.success(f"Your resume ATS compatibility score is **{max(score, 0)} / 100**.")

    st.success("✅ Your resume looks ATS-friendly!")

    # ATS Best Practices
    st.subheader("📌 ATS Optimization Tips")
    st.markdown("""
    - ✅ Use standard section headings like *Education*, *Experience*, *Skills*, etc.  
    - ✅ Stick to standard fonts like Arial, Calibri, or Times New Roman.  
    - ❌ Avoid text boxes, tables, columns, images, or charts.  
    - ✅ Submit in PDF format unless instructed otherwise.  
    - ✅ Include relevant keywords from the job description.  
    """)

    # Back to dashboard
    if st.button("🔙 Back to Dashboard"):
        st.session_state["selected_module"] = None
        st.rerun()
