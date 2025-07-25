import streamlit as st

def render_career_path():
    st.markdown("<h2 style='color:#1B5E20;'>🛤️ Career Path Suggestions</h2>", unsafe_allow_html=True)

    role = st.session_state.get("selected_role", "").title()

    # Sample roadmap structure (you can expand this based on role)
    roadmap = {
        "Entry Level": {
            "Title": f"Junior {role}",
            "Skills": [
                "Fundamentals of CS & coding",
                "Basic tools (e.g., Git, VSCode)",
                f"Beginner-level {role}-specific libraries",
                "Problem-solving & debugging"
            ]
        },
        "Mid Level": {
            "Title": f"{role}",
            "Skills": [
                "Advanced tools & frameworks",
                "Project architecture & scalability",
                "Collaboration in teams",
                "Testing & documentation"
            ]
        },
        "Senior Level": {
            "Title": f"Senior {role}",
            "Skills": [
                "System design & architecture",
                "Mentoring & code reviews",
                "Performance optimization",
                "Cross-functional collaboration"
            ]
        },
        "Lead/Manager": {
            "Title": f"{role} Lead / Manager",
            "Skills": [
                "Leadership & communication",
                "Team & project management",
                "Stakeholder coordination",
                "Strategic planning & vision"
            ]
        }
    }

    for level, details in roadmap.items():
        st.markdown(f"""
            <div style='border: 2px solid #A5D6A7; border-radius: 10px; padding: 15px; margin-bottom: 20px; background-color: #E8F5E9;'>
                <h4 style='color:#2E7D32;'>{level} – <i>{details["Title"]}</i></h4>
                <ul>
                    {"".join([f"<li>{skill}</li>" for skill in details["Skills"]])}
                </ul>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("### 💡 Learning Tips")
    st.markdown("""
    - Set measurable goals for each level (e.g., build 3 projects, contribute to open source).
    - Stay consistent with learning & upskilling using platforms like Coursera, Udemy, or GitHub.
    - Build your portfolio and update your resume as you grow.
    """)

    if st.button("🔙 Back to Dashboard"):
        st.session_state.selected_module = None
        st.rerun()
