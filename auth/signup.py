import streamlit as st
from auth.auth_db import add_user

def signup_ui():
    st.markdown("<h2 style='text-align:center; color:#004080;'>Sign Up</h2>", unsafe_allow_html=True)

    name = st.text_input("Full Name", placeholder="Enter your full name")
    email = st.text_input("Email", placeholder="Enter your email 📧")
    password = st.text_input("Password", type="password", placeholder="Create a password 🔒")
    confirm = st.text_input("Confirm Password", type="password", placeholder="Confirm your password 🔒")

    if st.button("Sign Up", key="signup"):
        if not name or not email or not password or not confirm:
            st.warning("Please fill out all fields.")
        elif password != confirm:
            st.error("Passwords do not match!")
        else:
            try:
                add_user(name, email, password)
                st.success("✅ Account created! Logging you in...")

                # 🔐 Auto-login the user by setting session state
                st.session_state.logged_in = True
                st.session_state.name = name
                st.session_state.auth_page = None  # Clear auth page
                st.experimental_rerun()  # 🔁 Go to dashboard flow

            except ValueError as ve:
                st.error(f"❌ {ve}")
            except Exception:
                st.error("❌ Something went wrong while creating the account.")
