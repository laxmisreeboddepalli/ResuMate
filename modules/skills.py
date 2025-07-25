# modules/skills.py

import streamlit as st

def render_skills():
    st.markdown("""
        <style>
            .section-header {
                font-size: 24px;
                font-weight: bold;
                color: #004080;
                margin-bottom: 10px;
            }
            .skill-badge {
                display: inline-block;
                background-color: #e3f2fd;
                color: #004080;
                padding: 8px 12px;
                margin: 5px;
                border-radius: 20px;
                font-size: 14px;
                font-weight: 500;
            }
            .back-button {
                text-align: center;
                margin-top: 30px;
            }
            .stButton > button {
                background-color: #1976d2 !important;
                color: white !important;
                border-radius: 10px !important;
                padding: 10px 20px !important;
                font-weight: bold;
                border: none;
                transition: all 0.2s ease-in-out;
            }
            .stButton > button:hover {
                transform: scale(1.05);
                background-color: #1565c0 !important;
            }
        </style>
    """, unsafe_allow_html=True)

    parsed = st.session_state.get("parsed_resume_data", {})
    job_role = st.session_state.get("selected_role", "").lower()
    raw_text = parsed.get("raw_text", "")

    if not parsed:
        st.warning("Please upload a resume first.")
        return

    st.markdown("<div class='section-header'>🧠 Skills You Have</div>", unsafe_allow_html=True)
    found_skills = extract_skills(raw_text)
    if found_skills:
        skill_html = "".join([f"<span class='skill-badge'>{skill}</span>" for skill in found_skills])
        st.markdown(skill_html, unsafe_allow_html=True)
    else:
        st.info("No clear skills found in resume.")

    st.markdown("<div class='section-header'>✅ Recommended Skills to Add</div>", unsafe_allow_html=True)
    suggestions = get_recommended_skills(job_role)
    to_add = list(set(suggestions) - set(found_skills))
    if to_add:
        skill_html = "".join([f"<span class='skill-badge'>{skill}</span>" for skill in to_add])
        st.markdown(skill_html, unsafe_allow_html=True)
    else:
        st.success("You're well-equipped for this role!")

    st.markdown("<div class='section-header'>❌ Skills to Remove (Irrelevant)</div>", unsafe_allow_html=True)
    to_remove = list(set(found_skills) - set(suggestions))
    if to_remove:
        skill_html = "".join([f"<span class='skill-badge'>{skill}</span>" for skill in to_remove])
        st.markdown(skill_html, unsafe_allow_html=True)
    else:
        st.info("All listed skills are relevant!")

    with st.container():
        st.markdown("<div class='back-button'>", unsafe_allow_html=True)
        if st.button("🔙 Back to Dashboard"):
            st.session_state.selected_module = None
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

def extract_skills(text):
    SKILL_KEYWORDS = [
        "python", "java", "c++", "sql", "html", "css", "javascript",
        "machine learning", "deep learning", "pandas", "numpy",
        "tensorflow", "keras", "scikit-learn", "flask", "django",
        "react", "node", "git", "github", "linux", "excel", "power bi"
    ]
    found = []
    for skill in SKILL_KEYWORDS:
        if skill.lower() in text.lower():
            found.append(skill.title())
    return found

def get_recommended_skills(role):
    role = role.lower()
    SKILL_MAP = {
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

    for r in SKILL_MAP:
        if r.lower() in role:
            return SKILL_MAP[r]
    return []
