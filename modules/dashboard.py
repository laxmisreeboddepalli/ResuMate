# modules/dashboard.py

import streamlit as st

from modules.user_info import render_user_info
from modules.skills import render_skills
from modules.resources import render_resources
from modules.video_recommendations import render_video_recommendations
from modules.resume_score_tips import render_resume_score_tips
from modules.ats_checker import render_ats_checker
from modules.career_path import render_career_path
from modules.cover_letter import render_cover_letter
from modules.job_readiness_analyzer import render_job_readiness_analyzer
from modules.projects_experience_review import render_projects_experience_review
from modules.summary import render_summary
from modules.visual_dashboard import render_visual_dashboard

def show_dashboard(role):
    st.set_page_config(page_title="Dashboard", layout="wide")

    selected = st.session_state.get("selected_module", None)

    if selected == "user_info":
        render_user_info()
        return
    elif selected == "skills":
        render_skills()
        return
    elif selected == "resources":
        render_resources()
        return
    elif selected == "video_recommendations":
        render_video_recommendations()
        return
    elif selected == "ats_checker":
        render_ats_checker()
        return
    elif selected == "career_path":
        render_career_path()
        return
    elif selected == "cover_letter":
        render_cover_letter()
        return
    elif selected == "job_readiness_analyzer":
        render_job_readiness_analyzer()
        return
    elif selected == "projects_experience_review":
        render_projects_experience_review()
        return
    elif selected == "resume_score_tips":
        render_resume_score_tips()
        return
    elif selected == "summary":
        render_summary()
        return
    elif selected == "visual_dashboard":
        render_visual_dashboard()
        return

    with st.sidebar:
        st.markdown("""
            <style>
                .sidebar-top {
                    text-align: center;
                    margin-top: 20px;
                    margin-bottom: 60px;
                }
                .sidebar-subtitle {
                    font-size: 14px;
                    color: #333;
                    margin-bottom: 10px;
                }
                .sidebar-header {
                    font-size: 22px;
                    font-weight: bold;
                    color: #004080;
                }
                .sidebar-footer {
                    position: fixed;
                    bottom: 30px;
                    left: 15px;
                    width: 220px;
                    font-size: 18px;
                    font-weight: bold;
                    color: #4A148C;
                    text-align: center;
                }
                section[data-testid="stSidebar"] {
                    overflow: hidden !important;
                }
            </style>

            <div class='sidebar-top'>
                <div class='sidebar-subtitle'>Your career assistant</div>
                <div class='sidebar-header'>USER NAME - {name}</div>
            </div>
            <div class='sidebar-footer'>
                BY LAXMISREE BODDEPALLI
            </div>
        """.replace("{name}", st.session_state.get("name", "User")), unsafe_allow_html=True)

    # Styles for cards
    st.markdown("""
        <style>
            .dashboard-title {
                text-align: center;
                font-size: 36px;
                font-weight: bold;
                color: #004080;
                margin-bottom: 30px;
            }
            .dashboard-card {
                background: #f0f8ff;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                transition: transform 0.2s ease, background-color 0.2s ease;
                text-align: center;
                height: 150px;
                cursor: pointer;
            }
            .dashboard-card:hover {
                transform: translateY(-5px);
                background-color: #d2ecfc;
            }
            .dashboard-card.selected {
                background-color: #bbdefb !important;
            }
            .card-title {
                font-size: 20px;
                color: #004080;
                font-weight: bold;
            }
            .card-description {
                font-size: 14px;
                color: #333;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown(f"<div class='dashboard-title'>🎯 Dashboard for {role}</div>", unsafe_allow_html=True)

    # Cards list
    cards = [
        ("user_info", " User Information", "View your basic profile details"),
        ("skills", " Skills", "Skills you have vs needed"),
        ("visual_dashboard", " Visual Dashboard", "Graphs based on your skills"),
        ("resources", " Resources", "Courses & certificates to add/remove"),
        ("video_recommendations", " Video Recommendations", "Auto-recommended videos"),
        ("projects_experience_review", " Projects & Experience Review", "Suggestions for what to keep/remove"),
        ("resume_score_tips", " Resume Score & Tips", "Analyze resume formatting and tone"),
        ("cover_letter", " Cover Letter Generator", "Auto-generate cover letter"),
        ("ats_checker", " ATS Compatibility Checker", "Check if your resume is ATS-friendly"),
        ("job_readiness_analyzer", " Job Readiness Analyzer", "check your readiness for the selected role"),
        ("career_path", " Career Path Suggestions", "Roadmap based on job role"),
        ("summary", " Summary Feedback", "summary & suggestions")
    ]

    for row in range(0, len(cards), 3):
        cols = st.columns(3)
        for i in range(3):
            if row + i < len(cards):
                key, title, desc = cards[row + i]
                selected_class = "selected" if selected == key else ""
                with cols[i]:
                    clicked = st.button(
                        label=f"\n\n",  # invisible label
                        key=f"btn_{key}",
                        help=title,
                    )
                    st.markdown(f"""
                        <div class='dashboard-card {selected_class}'>
                            <div class='card-title'>{title}</div>
                            <div class='card-description'>{desc}</div>
                        </div>
                    """, unsafe_allow_html=True)
                    if clicked:
                        st.session_state["selected_module"] = key
                        st.rerun()
