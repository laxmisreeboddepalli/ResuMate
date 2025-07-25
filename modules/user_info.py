# modules/user_info.py

import streamlit as st

def render_user_info():
    st.markdown("""
        <style>
            .info-card {
                background: #f0f8ff;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px;
            }
            .info-title {
                font-size: 20px;
                color: #004080;
                font-weight: bold;
            }
            .info-value {
                font-size: 16px;
                color: #333;
            }
            .info-value a {
                color: #1976d2;
                text-decoration: none;
            }
            .dashboard-button {
                display: flex;
                justify-content: center;
                margin-top: 30px;
            }
        </style>
    """, unsafe_allow_html=True)

    data = st.session_state.get("parsed_resume_data", {})

    if not data:
        st.warning("Please upload a resume first.")
        return

    # Sanitize name if it contains email
    raw_name = data.get("name", "N/A")
    email = data.get("email", "")
    if email and email in raw_name:
        name = raw_name.replace(email, "").replace("(", "").replace(")", "").strip()
    else:
        name = raw_name

    st.markdown("<h3 style='text-align:center; color:#004080;'>👤 User Information</h3>", unsafe_allow_html=True)

    fields = {
        "Name": name,
        "Email": f"<a href='mailto:{email}'>{email}</a>" if email and email != "N/A" else "N/A",
        "Phone Number": data.get("phone", "N/A"),
        "Number of Pages": data.get("num_pages", "N/A"),
    }

    for label, value in fields.items():
        st.markdown(f"""
            <div class='info-card'>
                <div class='info-title'>{label}</div>
                <div class='info-value'>{value}</div>
            </div>
        """, unsafe_allow_html=True)

    # Back to Dashboard button
    st.markdown("""
        <div class='dashboard-button'>
    """, unsafe_allow_html=True)
    if st.button("⬅️ Back to Dashboard"):
        st.session_state.selected_module = None
        st.rerun()
    st.markdown("""</div>""", unsafe_allow_html=True)
