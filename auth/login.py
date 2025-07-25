import streamlit as st
from auth.auth_db import verify_user

def login_ui():
    st.subheader("Login")

    email = st.text_input("Email", placeholder="Enter your email 📧")
    password = st.text_input("Password", type="password", placeholder="Enter your password 🔒")

    if st.button("Login", key="login"):
        user = verify_user(email, password)
        if user:
            st.session_state.logged_in = True
            st.session_state.name = user[1]  # user[1] = name
            st.success(f"Welcome back, {user[1]}!")
        else:
            st.error("Invalid email or password.")
