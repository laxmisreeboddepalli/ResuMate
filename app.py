import streamlit as st
from auth.auth_db import create_users_table
from auth.signup import signup_ui
from auth.login import login_ui
from utils.resume_uploader import resume_uploader_ui
from utils.job_suggester import job_selector_ui
from modules.dashboard import show_dashboard

# ✅ Init DB
create_users_table()

# ✅ Session State Setup
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "name" not in st.session_state:
    st.session_state.name = ""
if "auth_page" not in st.session_state:
    st.session_state.auth_page = "signup"

# ✅ Page Config
st.set_page_config(page_title="ResuMate", layout="centered")

# ✅ Custom CSS
st.markdown("""<style>
    [data-testid="stSidebar"] {
        background-color: #e3f2fd;
    }
    .sidebar-box {
        background-color: #d0e6fa;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
    }
    .main-header {
        text-align: center;
        margin-top: -40px;
    }
    .main-title {
        font-size: 48px;
        background-color: #f0f2f6;
        color: #004080;
        padding: 20px;
        border-radius: 15px;
    }
    .sub-title {
        font-size: 20px;
        color: #444;
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
    .stButton > button:active {
        transform: scale(0.98);
    }
    input[type="text"], input[type="email"], input[type="password"] {
        transition: 0.2s ease;
    }
    input[type="text"]:hover, input[type="email"]:hover, input[type="password"]:hover {
        border: 2px solid #42a5f5 !important;
        transform: scale(1.01);
    }
    input[type="file"]::file-selector-button {
        background-color: #1976d2;
        color: white;
        padding: 10px 16px;
        border-radius: 8px;
        border: none;
        font-weight: bold;
        cursor: pointer;
    }
    input[type="file"]::file-selector-button:hover {
        background-color: #1565c0;
    }
</style>""", unsafe_allow_html=True)

# ✅ Sidebar
with st.sidebar:
    st.markdown("""
        <div class='sidebar-box'>
            <h2 style='color:#004080;'>ResuMate</h2>
            <p style='color:#333;'>Smart Resume Analyzer</p>
        </div>
        <div class='sidebar-footer' style='text-align:center; margin-top: 20px; font-weight: bold; color:#004080;'>
            BY LAXMISREE BODDEPALLI       
        </div>
    """, unsafe_allow_html=True)

# ✅ Main Header
st.markdown("""
    <div class='main-header'>
        <h1 class='main-title'>ResuMate</h1>
        <p class='sub-title'>Welcome to ResuMate – Smart Resume Analyzer</p>
    </div>
    <br>
""", unsafe_allow_html=True)

# ✅ Main Logic
if st.session_state.logged_in:
    st.success(f"🎉 Logged in as: {st.session_state.name}")

    if "selected_role" in st.session_state:
        show_dashboard(st.session_state.selected_role)
    else:
        resume_text = resume_uploader_ui()
        if resume_text:
            job_selector_ui(resume_text)
else:
    if st.session_state.auth_page == "signup":
        signup_ui()
        st.markdown("<p style='text-align:center;'>Already have an account?</p>", unsafe_allow_html=True)
        if st.button("Go to Login"):
            st.session_state.auth_page = "login"
    else:
        login_ui()
        st.markdown("<p style='text-align:center;'>Don't have an account?</p>", unsafe_allow_html=True)
        if st.button("Go to Sign Up"):
            st.session_state.auth_page = "signup"
