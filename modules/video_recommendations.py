# modules/video_recommendations.py

import streamlit as st

VIDEO_RECOMMENDATIONS = {
    "ml engineer": [
        ("Machine Learning Roadmap for 2024", "https://www.youtube.com/watch?v=OdhtkODF1lA"),
        ("ML Engineer vs Data Scientist | Career Comparison", "https://www.youtube.com/watch?v=O7bD_3aY6Io"),
        ("Top 5 ML Projects for Resume", "https://www.youtube.com/watch?v=lI1ae4REbFM"),
        ("TensorFlow Crash Course", "https://www.youtube.com/watch?v=tPYj3fFJGjk"),
        ("End-to-End ML Project", "https://www.youtube.com/watch?v=7eh4d6sabA0"),
        ("How to Become an ML Engineer", "https://www.youtube.com/watch?v=1vsmaEfbno0"),
        ("Scikit-Learn Tutorial", "https://www.youtube.com/watch?v=pqNCD_5r0IU"),
        ("Top 10 ML Tools", "https://www.youtube.com/watch?v=aircAruvnKk")
    ],
    "frontend developer": [
        ("Frontend Developer Roadmap 2024", "https://www.youtube.com/watch?v=zJSY8tbf_ys"),
        ("Responsive Web Design Full Course", "https://www.youtube.com/watch?v=srvUrASNj0s"),
        ("10 Frontend Projects for Resume", "https://www.youtube.com/watch?v=BOxVy9gJ3uA"),
        ("React Full Course", "https://www.youtube.com/watch?v=bMknfKXIFA8"),
        ("CSS Flexbox and Grid Tutorial", "https://www.youtube.com/watch?v=JJSoEo8JSnc"),
        ("JavaScript DOM Crash Course", "https://www.youtube.com/watch?v=0ik6X4DJKCc"),
        ("Tailwind CSS Crash Course", "https://www.youtube.com/watch?v=ft30zcMlFao"),
        ("How to Become a Frontend Dev", "https://www.youtube.com/watch?v=7s6Y3rgnFaw")
    ],
    "backend developer": [
        ("Backend Developer Roadmap 2024", "https://www.youtube.com/watch?v=0m8K7Wf3rWg"),
        ("What is REST API?", "https://www.youtube.com/watch?v=Q-BpqyOT3a8"),
        ("Backend Projects for Resume", "https://www.youtube.com/watch?v=ePpZkFhKxkI"),
        ("Django Tutorial for Beginners", "https://www.youtube.com/watch?v=F5mRW0jo-U4"),
        ("Flask Crash Course", "https://www.youtube.com/watch?v=Z1RJmh_OqeA"),
        ("Node.js Full Course", "https://www.youtube.com/watch?v=Oe421EPjeBE"),
        ("PostgreSQL Crash Course", "https://www.youtube.com/watch?v=qw--VYLpxG4"),
        ("How to Become a Backend Dev", "https://www.youtube.com/watch?v=2lsK_aLvvh4")
    ],
    "cloud engineer": [
        ("Cloud Computing Full Course", "https://www.youtube.com/watch?v=2LaAJq1lB1Q"),
        ("AWS vs Azure vs Google Cloud", "https://www.youtube.com/watch?v=i_LwzRVP7bg"),
        ("Top 5 Cloud Projects", "https://www.youtube.com/watch?v=b3wK0U2dE5w"),
        ("AWS Crash Course", "https://www.youtube.com/watch?v=ulprqHHWlng"),
        ("GCP Basics", "https://www.youtube.com/watch?v=1i-r8YpY3gI"),
        ("Azure Full Course", "https://www.youtube.com/watch?v=iznOEoYHj1I"),
        ("Cloud Security Basics", "https://www.youtube.com/watch?v=kh4J2JrWiUo"),
        ("Cloud Career Paths", "https://www.youtube.com/watch?v=2LaAJq1lB1Q")
    ],
    "devops engineer": [
        ("DevOps Full Course in 8 Hours", "https://www.youtube.com/watch?v=0yWAtQ6wYNM"),
        ("What is CI/CD?", "https://www.youtube.com/watch?v=scEDHsr3APg"),
        ("DevOps Roadmap 2024", "https://www.youtube.com/watch?v=0yWAtQ6wYNM"),
        ("Docker Crash Course", "https://www.youtube.com/watch?v=pTFZFxd4hOI"),
        ("Kubernetes Tutorial", "https://www.youtube.com/watch?v=X48VuDVv0do"),
        ("Jenkins Explained", "https://www.youtube.com/watch?v=FX322RVNGj4"),
        ("Terraform Crash Course", "https://www.youtube.com/watch?v=V4waklkBC38"),
        ("DevOps Tools Overview", "https://www.youtube.com/watch?v=FZMyb9yOa_s")
    ],
    "ui ux designer": [
        ("UI/UX Design for Beginners", "https://www.youtube.com/watch?v=3Yp3CN3fTjM"),
        ("How to Become a UX Designer", "https://www.youtube.com/watch?v=5eQG3wz6I0g"),
        ("UI Design Crash Course", "https://www.youtube.com/watch?v=9B7yUw1l8b4"),
        ("Figma Tutorial", "https://www.youtube.com/watch?v=FTFaQWZBqQ8"),
        ("Design Thinking Explained", "https://www.youtube.com/watch?v=_r0VX-aU_T8"),
        ("Wireframing Basics", "https://www.youtube.com/watch?v=pU6M6Ncsgig"),
        ("UX Research Methods", "https://www.youtube.com/watch?v=8A2t_tAjMz8"),
        ("UI/UX Career Tips", "https://www.youtube.com/watch?v=9B7yUw1l8b4")
    ],
    "data analyst": [
        ("Data Analyst Roadmap 2024", "https://www.youtube.com/watch?v=GcXcSZ0gQps"),
        ("Excel to MySQL: Data Analytics", "https://www.youtube.com/watch?v=9RUOnP-uooc"),
        ("Top 5 Data Analyst Projects", "https://www.youtube.com/watch?v=LvZcxz5uvF8"),
        ("SQL for Data Analysis Full Course", "https://www.youtube.com/watch?v=4b4MUYve_U8"),
        ("Tableau Full Course for Beginners", "https://www.youtube.com/watch?v=2TR3xKzXg1I"),
        ("Power BI Full Course - Learn Power BI in 4 Hours", "https://www.youtube.com/watch?v=AGrl-H87pRU"),
        ("Statistics for Data Science", "https://www.youtube.com/watch?v=xxpc-HPKN28"),
        ("How to Become a Data Analyst in 2024", "https://www.youtube.com/watch?v=wX6s-NpDhKE"),
        ("Python for Data Analysis - Full Course", "https://www.youtube.com/watch?v=Gp3XaJwXvCo"),
        ("Career Talk: Day in the Life of a Data Analyst", "https://www.youtube.com/watch?v=2rmN9D6h9yI"),
        ("Top Data Analyst Interview Questions & Answers", "https://www.youtube.com/watch?v=8g1JjjFkYkM"),
        ("Build a Portfolio as a Data Analyst", "https://www.youtube.com/watch?v=U4ZGxWbbN8Q")
    ],
    "ml engineer": [
        ("Machine Learning Roadmap for 2024", "https://www.youtube.com/watch?v=OdhtkODF1lA"),
        ("ML Engineer vs Data Scientist | Career Comparison", "https://www.youtube.com/watch?v=O7bD_3aY6Io"),
        ("Top 5 ML Projects for Resume", "https://www.youtube.com/watch?v=lI1ae4REbFM"),
        ("TensorFlow Tutorial for Beginners", "https://www.youtube.com/watch?v=tPYj3fFJGjk"),
        ("Deploying ML Models", "https://www.youtube.com/watch?v=6r5eqPxLwbE"),
        ("How to Become an ML Engineer", "https://www.youtube.com/watch?v=0Lt9w-BxKFQ"),
        ("ML Interview Prep", "https://www.youtube.com/watch?v=Zcd7jvMU1zQ"),
        ("ML Projects for Beginners", "https://www.youtube.com/watch?v=zbzjYv8E5zU")
    ],
    "frontend developer": [
        ("Frontend Developer Roadmap 2024", "https://www.youtube.com/watch?v=zJSY8tbf_ys"),
        ("Responsive Web Design Full Course", "https://www.youtube.com/watch?v=srvUrASNj0s"),
        ("10 Frontend Projects for Resume", "https://www.youtube.com/watch?v=BOxVy9gJ3uA"),
        ("JavaScript for Beginners", "https://www.youtube.com/watch?v=W6NZfCO5SIk"),
        ("React JS Crash Course", "https://www.youtube.com/watch?v=w7ejDZ8SWv8"),
        ("Advanced CSS and Sass", "https://www.youtube.com/watch?v=F0jzGdvJ9So"),
        ("Tailwind CSS in 100 Seconds", "https://www.youtube.com/watch?v=mr15Xzb1Ook"),
        ("Frontend Developer Interview Guide", "https://www.youtube.com/watch?v=rh5gINLBfIQ")
    ],
    "backend developer": [
        ("Backend Developer Roadmap 2024", "https://www.youtube.com/watch?v=0m8K7Wf3rWg"),
        ("What is REST API?", "https://www.youtube.com/watch?v=Q-BpqyOT3a8"),
        ("Backend Projects for Resume", "https://www.youtube.com/watch?v=ePpZkFhKxkI"),
        ("Flask Tutorial", "https://www.youtube.com/watch?v=Z1RJmh_OqeA"),
        ("Django Full Course", "https://www.youtube.com/watch?v=F5mRW0jo-U4"),
        ("Node.js Crash Course", "https://www.youtube.com/watch?v=fBNz5xF-Kx4"),
        ("Database Design Tutorial", "https://www.youtube.com/watch?v=ztHopE5Wnpc"),
        ("PostgreSQL Full Course", "https://www.youtube.com/watch?v=qw--VYLpxG4")
    ],
    "cloud engineer": [
        ("Cloud Computing Full Course", "https://www.youtube.com/watch?v=2LaAJq1lB1Q"),
        ("AWS vs Azure vs Google Cloud", "https://www.youtube.com/watch?v=i_LwzRVP7bg"),
        ("Top 5 Cloud Projects", "https://www.youtube.com/watch?v=b3wK0U2dE5w"),
        ("AWS Full Course", "https://www.youtube.com/watch?v=ulprqHHWlng"),
        ("Azure Full Course", "https://www.youtube.com/watch?v=izK6zDKUuGg"),
        ("GCP Basics", "https://www.youtube.com/watch?v=7Pnv2xWe7P4"),
        ("Serverless Architecture Explained", "https://www.youtube.com/watch?v=wQh5V7l5giU"),
        ("Deploy on AWS with Terraform", "https://www.youtube.com/watch?v=SLB_c_ayRMo")
    ],
    "product manager": [
        ("Product Manager Career Path", "https://www.youtube.com/watch?v=YnkzO-1uJ0Y"),
        ("PM vs Project Manager", "https://www.youtube.com/watch?v=lGzWn4ZnbQo"),
        ("What is Product Management?", "https://www.youtube.com/watch?v=gY2LDAK5LE8"),
        ("Agile & Scrum Explained", "https://www.youtube.com/watch?v=9TycLR0TqFA"),
        ("Roadmapping for PMs", "https://www.youtube.com/watch?v=yA5L8Oe7hYI"),
        ("How to Write a PRD", "https://www.youtube.com/watch?v=d-oz_2LwRzI"),
        ("PM Interview Questions", "https://www.youtube.com/watch?v=Y7n3MUM6rRQ"),
        ("PM Tools You Should Know", "https://www.youtube.com/watch?v=IQZkgaIkmLY")
    ],
    "business analyst": [
        ("Business Analyst Full Course", "https://www.youtube.com/watch?v=0G-K1hsnWXE"),
        ("What Business Analysts Do", "https://www.youtube.com/watch?v=1TZfCUzj3Rw"),
        ("SQL for Data Analysis", "https://www.youtube.com/watch?v=9Pzj7Aj25lw"),
        ("BA Interview Questions", "https://www.youtube.com/watch?v=cT_kI1sGb10"),
        ("Creating Use Cases", "https://www.youtube.com/watch?v=RSv3KqqZ-gM"),
        ("Data Visualization for BA", "https://www.youtube.com/watch?v=UI6lqHOVHic"),
        ("Stakeholder Management", "https://www.youtube.com/watch?v=YGVYAXMPN0I"),
        ("How to Create Wireframes", "https://www.youtube.com/watch?v=q-9NCrA7SQA")
    ],
    "quality assurance engineer": [
        ("QA Testing Full Course", "https://www.youtube.com/watch?v=5fD9X7GGdG8"),
        ("Manual Testing Tutorial", "https://www.youtube.com/watch?v=rvRrkTUcOYE"),
        ("Automation Testing with Selenium", "https://www.youtube.com/watch?v=wgNiGj1IlF0"),
        ("Bug Reporting Tools", "https://www.youtube.com/watch?v=7mK6Q2I3e5g"),
        ("JIRA for QA", "https://www.youtube.com/watch?v=4n0C7K4KKyI"),
        ("Writing Test Cases", "https://www.youtube.com/watch?v=BKzZ9DCEYoM"),
        ("QA Interview Preparation", "https://www.youtube.com/watch?v=I7fw5sY44IY"),
        ("Postman for API Testing", "https://www.youtube.com/watch?v=VywxIQ2ZXw4")
    ]
}


ROLE_ALIASES = {
    "machine learning engineer": "ml engineer",
    "ml engineering": "ml engineer",
    "frontend": "frontend developer",
    "frontend dev": "frontend developer",
    "backend": "backend developer",
    "backend dev": "backend developer",
    "cloud": "cloud engineer",
    "cloud dev": "cloud engineer",
    "devops": "devops engineer",
    "ios": "ios developer",
    "ios dev": "ios developer",
    "android": "android developer",
    "android dev": "android developer",
    "web": "web developer",
    "web dev": "web developer",
    "ui ux": "ui ux designer",
    "ux designer": "ui ux designer",
    "ui designer": "ui ux designer",
    "data analyst": "data analyst",
    "data analysis": "data analyst"
}

def render_video_recommendations():
    st.markdown("""
        <style>
            .section-header {
                font-size: 24px;
                font-weight: bold;
                color: #4a148c;
                margin-bottom: 10px;
            }
            .video-link {
                background-color: #f3e5f5;
                padding: 10px;
                border-radius: 10px;
                margin: 5px 0;
                font-size: 16px;
            }
        </style>
    """, unsafe_allow_html=True)

    role = st.session_state.get("selected_role", "").lower().strip()
    resolved_key = VIDEO_RECOMMENDATIONS.get(role)
    if not resolved_key:
        for alias, key in ROLE_ALIASES.items():
            if alias in role:
                resolved_key = VIDEO_RECOMMENDATIONS.get(key)
                break

    st.markdown("<div class='section-header'>📺 Recommended YouTube Videos</div>", unsafe_allow_html=True)

    if resolved_key:
        for title, link in resolved_key:
            st.markdown(f"<div class='video-link'>▶️ <a href='{link}' target='_blank'>{title}</a></div>", unsafe_allow_html=True)
    else:
        st.info("No video recommendations available for this role yet.")

    if st.button("🔙 Back to Dashboard"):
        st.session_state.selected_module = None
        st.rerun()
