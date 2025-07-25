# utils/job_suggester.py

import streamlit as st
import re
from collections import Counter

# ✅ Removed import of show_dashboard to prevent circular import
# from modules.dashboard import show_dashboard

# Sample dictionary of job roles and related keywords
role_keywords = {
    "Data Analyst": ["data analysis", "sql", "excel", "tableau", "power bi", "python", "statistics"],
    "Machine Learning Engineer": ["machine learning", "scikit-learn", "tensorflow", "keras", "model training", "neural networks"],
    "Frontend Developer": ["react", "html", "css", "javascript", "ui", "frontend", "tailwind"],
    "Backend Developer": ["nodejs", "django", "flask", "api", "mongodb", "mysql", "postgresql"],
    "DevOps Engineer": ["docker", "kubernetes", "ci/cd", "jenkins", "aws", "devops", "linux"],
    "UI/UX Designer": ["figma", "wireframes", "user research", "prototyping", "ux", "interface design"],
    "Business Analyst": ["business analysis", "excel", "data modeling", "requirements", "reporting", "dashboards"],
    "Cybersecurity Specialist": ["security", "penetration testing", "firewalls", "vulnerabilities", "network security", "ethical hacking"],
    "AI Researcher": ["deep learning", "nlp", "transformers", "pytorch", "research", "arxiv", "language models"],
    "Cloud Engineer": ["azure", "aws", "gcp", "cloud", "cloud architecture", "lambda"],
    "Mobile App Developer": ["android", "ios", "flutter", "react native", "mobile development"],
    "Product Manager": ["product management", "roadmap", "stakeholders", "user stories", "agile", "scrum"],
    "Full Stack Developer": ["frontend", "backend", "api", "javascript", "python", "react", "nodejs", "full stack"],
    "Data Engineer": ["data pipelines", "spark", "hadoop", "airflow", "etl", "big data", "sql", "data warehouse"],
    "Technical Support Engineer": ["troubleshooting", "support", "tickets", "windows", "linux", "helpdesk", "network"],
    "Digital Marketer": ["seo", "sem", "google ads", "social media", "email marketing", "analytics", "campaigns"],
    "HR Specialist": ["recruitment", "onboarding", "training", "hrms", "employee engagement", "talent management"],
    "Quality Assurance Engineer": ["testing", "test cases", "selenium", "bug tracking", "qa", "automation", "junit"],
    "Game Developer": ["unity", "unreal", "game design", "c#", "gameplay", "level design", "3d modeling"],
    "Graphic Designer": ["photoshop", "illustrator", "branding", "typography", "design", "creatives", "layout"],
    "Finance Analyst": ["financial modeling", "excel", "budgeting", "forecasting", "investments", "balance sheet"],
    "Technical Writer": ["documentation", "manuals", "api docs", "writing", "editing", "version control", "markdown"],
    "Content Writer": ["writing", "editing", "seo", "content creation", "blog", "copywriting"]
}

def suggest_job_roles_from_text(resume_text):
    text = resume_text.lower()
    role_scores = Counter()

    for role, keywords in role_keywords.items():
        for keyword in keywords:
            if re.search(rf"\b{re.escape(keyword)}\b", text):
                role_scores[role] += 1

    if not role_scores:
        return ["No strong match found. Try refining your resume."]

    top_roles = [role for role, _ in role_scores.most_common(5)]
    return top_roles

def job_selector_ui(resume_text):
    st.markdown("""<h3 style='color:#004080;'>💼 Job Role Suggestions</h3>""", unsafe_allow_html=True)

    suggestions = suggest_job_roles_from_text(resume_text)

    st.markdown("<b>🎯 Top Suggested Roles:</b>", unsafe_allow_html=True)

    # Show suggestions in a row
    cols = st.columns(len(suggestions))
    selected_role = None

    for i, role in enumerate(suggestions):
        if cols[i].button(role):
            selected_role = role

    # Or custom input
    custom_role = st.text_input("Or enter your own:")
    if custom_role and st.button("✅ Continue"):
        selected_role = custom_role

    # Redirect logic (but dashboard call happens in app.py)
    if selected_role:
        st.session_state.selected_role = selected_role
        st.session_state.show_dashboard = True
        st.rerun()
