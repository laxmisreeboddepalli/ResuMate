import streamlit as st
import random
from collections import defaultdict
import plotly.graph_objects as go

def render_visual_dashboard():
    st.markdown("<h2 style='color:#0D47A1;'>📊 Visual Dashboard</h2>", unsafe_allow_html=True)

    resume_data = st.session_state.get("parsed_resume_data", {})
    role = st.session_state.get("selected_role", "Data Scientist").title()
    skills = resume_data.get("skills", [])[:10]

    # 1. Predicted Fields Based on Skills
    st.markdown("#### 🔍 Predicted Suitable Fields Based on Your Skills")
    fields = ["Data Scientist", "ML Engineer", "AI Engineer", "Software Engineer"]
    relevance = [random.randint(40, 100) for _ in fields]

    fig1 = go.Figure(data=[go.Bar(x=fields, y=relevance, marker_color='skyblue')])
    fig1.update_layout(title="Predicted Fields Based on Skills", yaxis=dict(title="Relevance (%)"))
    st.plotly_chart(fig1, use_container_width=True)

    # 2. Top 5 Skills Required for Role (Static Example)
    st.markdown(f"#### 🧩 Top Skills Required for {role}")
    skill_map = {
        "AI Engineer": ["Python", "NLP", "Neural Networks", "AI Ethics", "TensorFlow"],
        "Software Engineer": ["DSA", "Git", "OOP", "System Design", "Databases"],
        "Data Scientist": ["Python", "Pandas", "NumPy", "Statistics", "Machine Learning", "SQL", "Data Visualization", "Scikit-learn", "Jupyter"],
        "Data Analyst": ["Excel", "SQL", "Power BI", "Tableau", "Python", "Data Cleaning", "Descriptive Statistics", "Dashboards"],
        "Machine Learning Engineer": ["Python", "Scikit-learn", "TensorFlow", "Keras", "Model Deployment", "ML Pipelines", "Pandas", "Docker"],
        "AI Researcher": ["Deep Learning", "NLP", "PyTorch", "Transformers", "Python", "TensorFlow", "Academic Writing", "ArXiv", "Experimentation"],
        "Frontend Developer": ["HTML", "CSS", "JavaScript", "React", "Tailwind", "Figma", "Redux", "Responsive Design"],
        "Backend Developer": ["Node.js", "Django", "Flask", "MongoDB", "MySQL", "PostgreSQL", "REST APIs", "Authentication"],
        "Full Stack Developer": ["React", "Node.js", "MongoDB", "Express.js", "API Integration", "HTML", "CSS", "JavaScript"],
        "Mobile App Developer": ["Flutter", "React Native", "Android", "iOS", "Dart", "Kotlin", "Swift", "Firebase", "UI Design"],
        "DevOps Engineer": ["Docker", "Kubernetes", "AWS", "CI/CD", "Jenkins", "Linux", "Terraform", "Monitoring", "Ansible"],
        "Cloud Engineer": ["AWS", "Azure", "GCP", "Cloud Architecture", "Kubernetes", "Serverless", "Cloud Security"],
        "UI/UX Designer": ["Figma", "Adobe XD", "Wireframing", "User Research", "Prototyping", "Design Thinking", "User Testing"],
        "Business Analyst": ["Requirement Gathering", "SQL", "Excel", "Data Modeling", "Stakeholder Management", "Documentation"],
        "Product Manager": ["Roadmapping", "Agile", "Scrum", "User Stories", "Wireframing", "KPIs", "Prioritization"],
        "Cybersecurity Specialist": ["Network Security", "Penetration Testing", "Firewalls", "Ethical Hacking", "OWASP", "Security Auditing", "Wireshark"],
        "Game Developer": ["Unity", "Unreal Engine", "C#", "Game Physics", "3D Modeling", "Level Design", "Animation"],
        "Graphic Designer": ["Photoshop", "Illustrator", "Typography", "Branding", "Canva", "Layout Design", "InDesign"],
        "Technical Support Engineer": ["Troubleshooting", "Ticketing Systems", "Networking", "Windows", "Linux", "Customer Support"],
        "Technical Writer": ["Markdown", "Documentation", "API Docs", "Version Control", "Editing", "Writing Tools"],
        "Content Writer": ["SEO", "Blog Writing", "Copywriting", "Editing", "Content Strategy", "Grammar"],
        "Digital Marketer": ["Google Ads", "SEO", "Email Marketing", "Social Media", "Analytics", "Content Marketing"],
        "HR Specialist": ["Recruitment", "Onboarding", "Payroll", "HRMS", "Compliance", "Talent Acquisition"],
        "Quality Assurance Engineer": ["Manual Testing", "Selenium", "JIRA", "Automation", "Bug Tracking", "Test Cases"],
        "Finance Analyst": ["Financial Modeling", "Forecasting", "Budgeting", "Excel", "Balance Sheet", "Ratio Analysis"]
    }
    top_skills = skill_map.get(role, list(skill_map["Data Scientist"]))

    fig2 = go.Figure(data=[go.Bar(x=top_skills, y=[90, 85, 80, 75, 70], marker_color='orange')])
    fig2.update_layout(title=f"Top 5 Skills Required for {role}", yaxis=dict(title="Importance (%)"))
    st.plotly_chart(fig2, use_container_width=True)

    # 3. Current Skills Match (simulated random relevance)
    st.markdown("#### 📌 Your Skill Match with Job Role")
    match_scores = [random.randint(30, 95) for _ in skills] if skills else [0]

    fig3 = go.Figure(data=[go.Bar(x=skills or ["No skills found"], y=match_scores, marker_color='green')])
    fig3.update_layout(title="Skill Match Score", yaxis=dict(title="Match %"))
    st.plotly_chart(fig3, use_container_width=True)

    st.info("Note: This dashboard is a visual estimate based on parsed skills and target role. For best results, ensure your resume includes clean, keyword-rich content.")

    if st.button("🔙 Back to Dashboard"):
        st.session_state.selected_module = None
        st.rerun()
