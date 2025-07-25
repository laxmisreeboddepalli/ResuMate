import streamlit as st

def show_sidebar_footer():
    # Only show once per session
    if "sidebar_footer_rendered" in st.session_state and st.session_state.sidebar_footer_rendered:
        return

    # Footer placement using HTML and inline CSS
    st.markdown("""
        <div style='position: fixed; bottom: 20px; left: 16px; color: #4A4A4A; font-size: 13px; opacity: 0.8;'>
            <hr style="margin-bottom: 4px;"/>
            <span>🔧 BY <strong>LAXMISREE BODDEPALLI</strong></span>
        </div>
    """, unsafe_allow_html=True)

    # Mark as rendered
    st.session_state.sidebar_footer_rendered = True
