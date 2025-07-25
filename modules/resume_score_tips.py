import streamlit as st
import re
import random
from modules.resources import ROLE_ALIASES

# Role-specific resume tips
ROLE_TIPS = {
    "data scientist": "Focus on Python, ML models, statistics, data visualization (Matplotlib, Seaborn), SQL. Show project impact using metrics.",
    "machine learning engineer": "Highlight model deployment, frameworks like TensorFlow/PyTorch, MLOps experience, and scalability of models.",
    "software developer": "Include GitHub links, use of frameworks (React, Django, Node.js), test coverage, and collaboration tools (Git).",
    "frontend developer": "Show React, HTML/CSS/JS skills, design implementation from Figma, mobile responsiveness, and performance optimization.",
    "backend developer": "Emphasize APIs, databases (SQL/NoSQL), authentication, server management, and scalability/security.",
    "full stack developer": "Combine frontend (React/Angular) and backend (Node/Django) skills. Include project architecture & deployment (Heroku, AWS).",
    "ui/ux designer": "Include Figma/Adobe XD work, design systems, wireframes, and focus on user research and accessibility improvements.",
    "project manager": "Highlight planning tools (JIRA/Trello), stakeholder management, Agile/Scrum, budget tracking, and delivery metrics.",
    "data analyst": "Show SQL, Excel, dashboards (Power BI, Tableau), and data storytelling. Quantify business insights and recommendations.",
    "business analyst": "Focus on gap analysis, business KPIs, stakeholder collaboration, tools like JIRA, and clear documentation.",
    "cloud engineer": "Mention AWS/Azure/GCP services used, automation with Terraform or CloudFormation, CI/CD pipelines, and system monitoring.",
    "devops engineer": "Highlight CI/CD, Docker, Kubernetes, Jenkins, monitoring/logging, and automation scripting (Bash, Python).",
    "cybersecurity analyst": "Show knowledge of threat detection, risk assessment, tools like Wireshark, and experience with audits or compliance.",
    "digital marketer": "Mention SEO, SEM, Google Analytics, campaign metrics (CTR, ROI), content strategies, and A/B testing experience.",
    "product manager": "Include product lifecycle management, market research, wireframes, KPIs tracked, and cross-functional leadership."
}

YOUTUBE_VIDEOS = [
    ("Write a Resume That Gets You Hired", "https://www.youtube.com/watch?v=ZQ-7OHyG8lI"),
    ("5 Resume Mistakes to Avoid", "https://www.youtube.com/watch?v=3NfBZu4Sf9w"),
    ("Resume Tips from Google Recruiters", "https://www.youtube.com/watch?v=BYn0GqjPPT8"),
    ("Improve Resume with ChatGPT", "https://www.youtube.com/watch?v=2q_4bG0Yw1M")
]

# ✅ Resume scoring logic (kept from original)
def score_resume(parsed_data):
    score = 0

    # Name
    score += 10 if parsed_data.get('name') else 0

    # Email
    score += 10 if parsed_data.get('email') else 0

    # Phone
    phone_score = 10 if parsed_data.get('phone') or re.search(r"\+?\d[\d\s\-\(\)]{8,}\d", parsed_data.get("raw_text", "")) else 0
    score += phone_score

    # Education
    education_keywords = ['bachelor', 'master', 'b.tech', 'm.tech', 'phd', 'degree', 'university', 'college']
    education_score = 15 if any(k in parsed_data.get("raw_text", "").lower() for k in education_keywords) else 0
    score += education_score

    # Experience
    experience_keywords = ['experience', 'internship', 'project', 'work']
    experience_score = 20 if any(k in parsed_data.get("raw_text", "").lower() for k in experience_keywords) else 0
    score += experience_score

    # Skills
    skills_score = 15 if parsed_data.get('skills') else 0
    score += skills_score

    # Formatting
    raw = parsed_data.get("raw_text", "")
    formatting_score = 20
    if len(raw) < 500:
        formatting_score -= 10
    if raw.count('•') < 3 and raw.count('-') < 3:
        formatting_score -= 5
    score += formatting_score

    return min(score, 100)


# ✅ Main UI function
def render_resume_score_tips():
    st.subheader("📊 Resume Score & Suggestions")

    parsed_data = st.session_state.get("parsed_resume_data", {})
    if not parsed_data:
        st.warning("⚠️ Please upload and parse a resume first.")
        return

    role = st.session_state.get("selected_role", "").lower()

    score = score_resume(parsed_data)
    st.markdown(f"""
        <div style="font-size: 24px; font-weight: bold; color: #004080;">
            ✅ Your resume score: <span style="color:#1976d2;">{score}/100</span>
        </div>
        <br>
    """, unsafe_allow_html=True)

    # ✍️ Formatting, Grammar & Language Suggestions
    st.subheader("✍️ Formatting, Grammar & Language Suggestions")
    st.markdown("""
    - Use clear, consistent bullet points and fonts.  
    - Keep it to 1 page (students/freshers) or 2 pages (experienced).  
    - Use strong action verbs and avoid long paragraphs.  
    - Avoid spelling/grammar errors — tools like Grammarly help.  
    - Replace vague terms like "good understanding" with achievements.
    """)

    # 🧠 Writing Tone Analysis
    st.subheader("🧠 Writing Tone Analysis")
    st.markdown("""
    - Maintain a confident and professional tone.  
    - Avoid being too modest or too casual.  
    - Emphasize impact using numbers, tools, or outcomes.
    """)

    # 🎯 Role-Specific Tips
    st.subheader("🎯 Role-Specific Resume Tips")

    # Step 1: Get role and apply alias mapping
    role = st.session_state.get("selected_role", "").lower()

    # Step 2: Remap using ROLE_ALIASES if defined
    for alias, mapped_role in st.session_state.get("ROLE_ALIASES", {}).items():
        if alias.lower() in role:
            role = mapped_role.lower()
            break

    # Step 3: Match exactly or partially
    matched_tip = None
    if role in ROLE_TIPS:
        matched_tip = ROLE_TIPS[role]
    else:
        # Fallback: Partial match
        for key in ROLE_TIPS:
            if key in role:
                matched_tip = ROLE_TIPS[key]
                break

    if matched_tip:
        st.markdown(f"""
        <div style='
            background-color: #f0f8ff;
            border-left: 5px solid #1976d2;
            padding: 15px;
            border-radius: 10px;
            font-size: 16px;
        '>{matched_tip}</div>
        """, unsafe_allow_html=True)
    else:
        st.info("No specific tips available for this role.")


    # 📹 YouTube Tips
    st.subheader("📹 Resume Tips from YouTube")
    for title, url in random.sample(YOUTUBE_VIDEOS, 4):
        st.markdown(f"- 🔗 [{title}]({url})")

    # 🔙 Back to dashboard
    if st.button("🔙 Back to Dashboard"):
        st.session_state.selected_module = None
        st.rerun()
