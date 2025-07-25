# modules/resources.py

import streamlit as st

COURSE_RECOMMENDATIONS = {
    "data scientist": [
        ["Machine Learning Crash Course by Google [Free]", "https://developers.google.com/machine-learning/crash-course"],
        ["Machine Learning A-Z by Udemy", "https://www.udemy.com/course/machinelearning/"],
        ["Machine Learning by Andrew NG", "https://www.coursera.org/learn/machine-learning"],
        ["Data Scientist Master Program of Simplilearn (IBM)", "https://www.simplilearn.com/big-data-and-analytics/senior-data-scientist-masters-program-training"],
        ["Data Science Foundations: Fundamentals by LinkedIn", "https://www.linkedin.com/learning/data-science-foundations-fundamentals-5"],
        ["Data Scientist with Python", "https://www.datacamp.com/tracks/data-scientist-with-python"],
        ["Programming for Data Science with Python", "https://www.udacity.com/course/programming-for-data-science-nanodegree--nd104"],
        ["Programming for Data Science with R", "https://www.udacity.com/course/programming-for-data-science-nanodegree-with-R--nd118"],
        ["Introduction to Data Science", "https://www.udacity.com/course/introduction-to-data-science--cd0017"],
        ["Intro to Machine Learning with TensorFlow", "https://www.udacity.com/course/intro-to-machine-learning-with-tensorflow-nanodegree--nd230"],
        ["IBM Data Science", "https://www.coursera.org/professional-certificates/ibm-data-science"],
        ["Python for Data Science and Machine Learning Bootcamp", "https://www.udemy.com/course/python-for-data-science-and-machine-learning-bootcamp/"]
    ],
    "web developer": [
        ["Django Crash course [Free]", "https://youtu.be/e1IyzVyrLSU"],
        ["Python and Django Full Stack Web Developer Bootcamp", "https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp"],
        ["React Crash Course [Free]", "https://youtu.be/Dorf8i6lCuk"],
        ["ReactJS Project Development Training", "https://www.dotnettricks.com/training/masters-program/reactjs-certification-training"],
        ["Full Stack Web Developer - MEAN Stack", "https://www.simplilearn.com/full-stack-web-developer-mean-stack-certification-training"],
        ["Node.js and Express.js [Free]", "https://youtu.be/Oe421EPjeBE"],
        ["Flask: Develop Web Applications in Python", "https://www.educative.io/courses/flask-develop-web-applications-in-python"],
        ["Full Stack Web Developer by Udacity", "https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044"],
        ["Front End Web Developer by Udacity", "https://www.udacity.com/course/front-end-web-developer-nanodegree--nd0011"],
        ["Become a React Developer by Udacity", "https://www.udacity.com/course/react-nanodegree--nd019"],
        ["The Web Developer Bootcamp 2023", "https://www.udemy.com/course/the-web-developer-bootcamp/"],
        ["HTML, CSS, and Javascript for Web Developers", "https://www.coursera.org/learn/html-css-javascript-for-web-developers"],
        ["Responsive Web Design Certification", "https://www.freecodecamp.org/learn/"]
    ],
    "android developer": [
        ["Android Development for Beginners [Free]", "https://youtu.be/fis26HvvDII"],
        ["Android App Development Specialization", "https://www.coursera.org/specializations/android-app-development"],
        ["Associate Android Developer Certification", "https://grow.google/androiddev/#?modal_active=none"],
        ["Become an Android Kotlin Developer by Udacity", "https://www.udacity.com/course/android-kotlin-developer-nanodegree--nd940"],
        ["Android Basics by Google", "https://www.udacity.com/course/android-basics-nanodegree-by-google--nd803"],
        ["The Complete Android Developer Course", "https://www.udemy.com/course/complete-android-n-developer-course/"],
        ["Building an Android App with Architecture Components", "https://www.linkedin.com/learning/building-an-android-app-with-architecture-components"],
        ["Android App Development Masterclass using Kotlin", "https://www.udemy.com/course/android-oreo-kotlin-app-masterclass/"],
        ["Flutter & Dart - The Complete Flutter App Development Course", "https://www.udemy.com/course/flutter-dart-the-complete-flutter-app-development-course/"],
        ["Flutter App Development Course [Free]", "https://youtu.be/rZLR5olMR64"]
    ],
    "ml engineer": [
        ["Machine Learning Engineering for Production (MLOps)", "https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops"],
        ["Deep Learning Specialization", "https://www.coursera.org/specializations/deep-learning"],
        ["ML & Deep Learning Bootcamp", "https://www.udemy.com/course/machinelearning/"],
        ["ML Engineer Career Track", "https://www.datacamp.com/tracks/machine-learning-scientist-with-python"],
        ["Advanced Machine Learning Specialization", "https://www.coursera.org/specializations/aml"],
        ["AI & ML Engineering Career Path", "https://www.codecademy.com/learn/paths/machine-learning-engineer-career-path"],
        ["TensorFlow Developer Certificate", "https://www.tensorflow.org/certificate"],
        ["Machine Learning by Andrew Ng", "https://www.coursera.org/learn/machine-learning"],
        ["DeepLearning.AI TensorFlow Developer", "https://www.coursera.org/professional-certificates/tensorflow-in-practice"],
        ["ML Engineering for Production (MLOps)", "https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops"],
        ["Practical Deep Learning for Coders (fast.ai)", "https://course.fast.ai"],
        ["Scikit‑learn & TensorFlow Documentation", "https://scikit-learn.org and https://www.tensorflow.org"]

    ],
    "devops engineer": [
        ["DevOps on AWS Specialization", "https://www.coursera.org/specializations/aws-devops"],
        ["CI/CD Pipelines with Jenkins", "https://www.udemy.com/course/jenkins-pipeline-as-code/"],
        ["Docker and Kubernetes: The Complete Guide", "https://www.udemy.com/course/docker-and-kubernetes-the-complete-guide/"],
        ["DevOps Engineer Career Path", "https://www.codecademy.com/learn/paths/devops-engineer-career-path"],
        ["Google Cloud DevOps and SRE", "https://www.coursera.org/specializations/site-reliability-engineering-sre-devops"],
        ["Docker Mastery (Udemy)", "https://www.udemy.com/course/docker-mastery"],
        ["Learn Kubernetes (KodeKloud)", "https://kodekloud.com/courses/kubernetes-for-beginners"],
        ["CI/CD with Jenkins (Udemy)", "https://www.udemy.com/course/learn-devops-ci-cd-with-jenkins-using-pipelines-and-docker"],
        ["AWS Certified DevOps Engineer Learning Path", "https://aws.amazon.com/certification/certified-devops-engineer-professional/"],
        ["The Linux Command Line Bootcamp", "https://www.udemy.com/course/linux-command-line"]
    ],
    "ios developer": [
        ["IOS App Development by LinkedIn", "https://www.linkedin.com/learning/subscription/topics/ios"],
        ["iOS & Swift - The Complete iOS App Development Bootcamp", "https://www.udemy.com/course/ios-13-app-development-bootcamp/"],
        ["Become an iOS Developer", "https://www.udacity.com/course/ios-developer-nanodegree--nd003"],
        ["iOS App Development with Swift Specialization", "https://www.coursera.org/specializations/app-development"],
        ["Mobile App Development with Swift", "https://www.edx.org/professional-certificate/curtinx-mobile-app-development-with-swift"],
        ["Swift Course by LinkedIn", "https://www.linkedin.com/learning/subscription/topics/swift-2"],
        ["Objective-C Crash Course for Swift Developers", "https://www.udemy.com/course/objectivec/"],
        ["Learn Swift by Codecademy", "https://www.codecademy.com/learn/learn-swift"],
        ["Swift Tutorial - Full Course for Beginners [Free]", "https://youtu.be/comQ1-x2a1Q"],
        ["Learn Swift Fast - [Free]", "https://youtu.be/FcsY1YPBwzQ"]
    ],
    "cloud engineer": [
        ["Google Cloud Engineering", "https://www.coursera.org/professional-certificates/cloud-engineering-gcp"],
        ["AWS Certified Solutions Architect", "https://www.udemy.com/course/aws-certified-solutions-architect-associate/"],
        ["Microsoft Azure Fundamentals", "https://www.coursera.org/learn/azure-fundamentals"],
        ["Become a Cloud DevOps Engineer", "https://www.udacity.com/course/cloud-dev-ops-nanodegree--nd9991"],
        ["Introduction to Cloud Computing", "https://cognitiveclass.ai/courses/introduction-to-cloud"],
        ["AWS Fundamentals Specialization", "https://www.coursera.org/specializations/aws-fundamentals"]
    ],
    "frontend developer": [
        ["The Complete React Developer", "https://www.udemy.com/course/complete-react-developer-zero-to-mastery/"],
        ["Modern HTML & CSS From The Beginning", "https://www.udemy.com/course/modern-html-css-from-the-beginning/"],
        ["JavaScript Basics", "https://www.coursera.org/learn/javascript-basics"],
        ["Responsive Web Design", "https://www.freecodecamp.org/learn/responsive-web-design/"],
        ["Frontend Developer Career Path", "https://www.codecademy.com/learn/paths/front-end-engineer-career-path"],
        ["Frontend Web Development with React", "https://www.coursera.org/learn/front-end-react"],
        ["Meta Front-End Developer Certificate", "https://www.coursera.org/professional-certificates/meta-front-end-developer"],
        ["JavaScript30 (Wes Bos)", "https://javascript30.com"],
        ["TailwindCSS Documentation & Challenges", "https://tailwindcss.com"],
        ["Frontend Developer Roadmap", "https://roadmap.sh/frontend"]
    ],
    "data analyst": [
        ["Google Data Analytics Certificate", "https://www.coursera.org/professional-certificates/google-data-analytics"],
        ["Excel to MySQL: Data Analytics", "https://www.coursera.org/specializations/excel-mysql"],
        ["IBM Data Analyst Professional Certificate", "https://www.coursera.org/professional-certificates/ibm-data-analyst"],
        ["Data Analyst Bootcamp", "https://www.udemy.com/course/data-analyst-bootcamp"],
        ["Data Analysis with Python by freeCodeCamp", "https://www.freecodecamp.org/learn/data-analysis-with-python/"],
        ["SQL for Data Science", "https://www.coursera.org/learn/sql-for-data-science"],
        ["Data Analysis and Visualization with Python", "https://www.udemy.com/course/python-for-data-analysis-and-visualization"],
        ["Statistics for Data Science and Business Analysis", "https://www.udemy.com/course/statistics-for-data-science-and-business-analysis/"],
        ["Power BI Desktop for Business Intelligence", "https://www.udemy.com/course/microsoft-power-bi-up-running-with-power-bi-desktop/"],
        ["Data Analytics Real-World Projects in Python", "https://www.udemy.com/course/data-analytics-real-world-projects-in-python"],
        ["Introduction to Data Analytics (IBM)", "https://cognitiveclass.ai/courses/introduction-to-data-analytics"],
        ["Analyzing Data with Microsoft Power BI", "https://learn.microsoft.com/en-us/training/paths/analyze-data-power-bi/"],
        ["Business Analytics Specialization (Wharton)", "https://www.coursera.org/specializations/wharton-business-analytics"],
        ["Data Visualization with Tableau", "https://www.coursera.org/learn/data-visualization-tableau"]
    ],
    "backend developer": [
        ["Backend Developer Roadmap", "https://roadmap.sh/backend"],
        ["Django Full Stack Course", "https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/"],
        ["REST APIs with Flask and Python", "https://www.udemy.com/course/rest-api-flask-and-python/"],
        ["Node.js Backend Bootcamp", "https://www.udemy.com/course/nodejs-the-complete-guide/"],
        ["Backend Engineering Bootcamp", "https://www.boot.dev/"],
        ["Spring Framework - Java Backend", "https://www.udemy.com/course/spring-framework-5-beginner-to-guru/"],
        ["Node.js Developer Course (Udemy)", "https://www.udemy.com/course/the-complete-nodejs-developer-course-2"],
        ["Python Django Full-Stack Bootcamp", "https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp"],
        ["Designing RESTful APIs (Udacity)", "https://www.udacity.com/course/designing-restful-apis--ud388"],
        ["PostgreSQL for Everybody", "https://www.coursera.org/specializations/postgresql-for-everybody"]
    ],
    "ui ux designer": [
        ["Google UX Design Professional Certificate", "https://www.coursera.org/professional-certificates/google-ux-design"],
        ["UI / UX Design Specialization", "https://www.coursera.org/specializations/ui-ux-design"],
        ["The Complete App Design Course - UX, UI and Design Thinking", "https://www.udemy.com/course/the-complete-app-design-course-ux-and-ui-design/"],
        ["UX & Web Design Master Course: Strategy, Design, Development", "https://www.udemy.com/course/ux-web-design-master-course-strategy-design-development/"],
        ["DESIGN RULES: Principles + Practices for Great UI Design", "https://www.udemy.com/course/design-rules/"],
        ["Become a UX Designer by Udacity", "https://www.udacity.com/course/ux-designer-nanodegree--nd578"],
        ["Adobe XD Tutorial: User Experience Design Course [Free]", "https://youtu.be/68w2VwalD5w"],
        ["Adobe XD for Beginners [Free]", "https://youtu.be/WEljsc2jorI"],
        ["Adobe XD in Simple Way", "https://learnux.io/course/adobe-xd"],
        ["DesignLab UX Academy", "https://trydesignlab.com/ux-academy"],
        ["Adobe XD for Designers", "https://www.linkedin.com/learning/adobe-xd-essential-training"],
        ["Figma Crash Course", "https://www.youtube.com/watch?v=FTFaQWZBqQ8"],
        ["Interaction Design Foundation Courses", "https://www.interaction-design.org/courses"]
    ],
    "Business Analyst": [
        ["Business Analysis Fundamentals", "https://www.udemy.com/course/business-analysis-fundamentals"],
        ["Excel Data Analysis (Coursera)", "https://www.coursera.org/learn/excel-data-analysis"],
        ["Agile Business Analysis", "https://www.linkedin.com/learning/agile-business-analysis"],
        ["CBAP Certification Training", "https://www.udemy.com/course/cbap-certification-training"],
        ["BA Times Resources", "https://www.batimes.com"]
    ],
    "Cybersecurity Specialist": [
        ["Intro to Cybersecurity (Cisco)", "https://www.netacad.com/courses/cybersecurity"],
        ["Google Cybersecurity Certificate", "https://www.coursera.org/professional-certificates/google-cybersecurity"],
        ["CompTIA Security+ Certification", "https://www.comptia.org/certifications/security"],
        ["TryHackMe Labs", "https://tryhackme.com"],
        ["OWASP Top 10 Resources", "https://owasp.org/www-project-top-ten"]
    ],
    "AI Researcher": [
        ["Deep Learning Specialization", "https://www.coursera.org/specializations/deep-learning"],
        ["NLP Specialization", "https://www.coursera.org/specializations/natural-language-processing"],
        ["CS224n: NLP with Deep Learning", "http://web.stanford.edu/class/cs224n"],
        ["Papers with Code + arXiv", "https://paperswithcode.com"],
        ["fast.ai Practical AI for Coders", "https://course.fast.ai"]
    ],
    "Cloud Engineer": [
        ["AWS Cloud Practitioner Essentials", "https://aws.amazon.com/training/cloud-practitioner-essentials"],
        ["Microsoft Azure Fundamentals (AZ‑900)", "https://docs.microsoft.com/en-us/learn/certifications/exams/az-900"],
        ["Google Cloud Associate Engineer", "https://www.coursera.org/professional-certificates/gcp-cloud-engineer"],
        ["A Cloud Guru / Linux Academy Paths", "https://acloudguru.com/learn"],
        ["Cloud Resume Challenge", "https://www.cloudresumechallenge.dev"]
    ],
    "Mobile App Developer": [
        ["Flutter Bootcamp (Udemy)", "https://www.udemy.com/course/flutter-bootcamp-with-dart"],
        ["iOS with Swift (Coursera)", "https://www.coursera.org/specializations/app-development"],
        ["React Native Guide", "https://www.udemy.com/course/react-native-the-practical-guide"],
        ["Android with Kotlin (Google)", "https://developer.android.com/courses/kotlin-android-fundamentals"],
        ["Code With Andrea – Flutter Tutorials", "https://codewithandrea.com"]
    ],
    "Product Manager": [
        ["Digital Product Management (Coursera)", "https://www.coursera.org/learn/uva-darden-digital-product-management"],
        ["Product School Resources", "https://productschool.com/resources"],
        ["One Month PM Course", "https://www.onemonth.com/courses/product-management"],
        ["Agile Product Owner (LinkedIn)", "https://www.linkedin.com/learning/agile-product-owner-role"],
        ["ProductPlan Blog", "https://www.productplan.com/blog"]
    ],
    "Content Writer": [
        ["HubSpot Content Marketing Cert", "https://academy.hubspot.com/courses/content-marketing"],
        ["SEO Writing Masterclass", "https://www.udemy.com/course/seo-writing-masterclass"],
        ["Grammarly Handbook", "https://www.grammarly.com/handbook"],
        ["Copywriting Crash Course", "https://www.linkedin.com/learning/copywriting-essentials"],
        ["The Strategy of Content Marketing (Coursera)", "https://www.coursera.org/learn/content-marketing"]
    ],
    "Full Stack Developer": [
        ["Full Stack Open", "https://fullstackopen.com"],
        ["The Odin Project", "https://www.theodinproject.com"],
        ["Full‑Stack Web Dev with React (Coursera)", "https://www.coursera.org/specializations/full-stack-react"],
        ["CS50 Web Programming (edX)", "https://online-learning.harvard.edu/course/web-programming-python-javascript"],
        ["MongoDB University Full‑Stack Path", "https://university.mongodb.com/"]
    ],
    "Data Engineer": [
        ["Google Cloud Data Engineering", "https://www.coursera.org/specializations/gcp-data-engineering"],
        ["Data Engineering Zoomcamp", "https://github.com/data-engineering-zoomcamp"],
        ["Apache Airflow Fundamentals", "https://www.astronomer.io/courses/airflow-fundamentals"],
        ["Databricks Data Engineer Path", "https://www.databricks.com/learning/data-engineer"],
        ["IBM Data Engineering Cert", "https://www.coursera.org/professional-certificates/ibm-data-engineer"]
    ],
    "Technical Support Engineer": [
        ["Google IT Support Cert", "https://www.coursera.org/professional-certificates/google-it-support"],
        ["CompTIA A+ Certification", "https://www.comptia.org/certifications/a"],
        ["Linux Essentials (Cisco)", "https://www.netacad.com/courses/linux-essentials"],
        ["Intro to Networking (LinkedIn)", "https://www.linkedin.com/learning/learning-networking-foundations"],
        ["ITIL Foundation Training", "https://www.axelos.com/certifications/itil-service-management"]
    ],
    "Digital Marketer": [
        ["Google Digital Marketing & E-commerce", "https://www.coursera.org/professional-certificates/google-digital-marketing-ecommerce"],
        ["Meta Social Media Cert", "https://www.coursera.org/professional-certificates/meta-social-media-marketing"],
        ["HubSpot Inbound Marketing", "https://academy.hubspot.com/courses/inbound-marketing"],
        ["Google Ads Certification", "https://skillshop.withgoogle.com/"],
        ["Moz SEO Training", "https://moz.com/seo-training"]
    ],
    "HR Specialist": [
        ["Alison HR Management", "https://alison.com/course/diploma-in-human-resources"],
        ["SHRM Cert Prep", "https://www.udemy.com/course/shrm-ca-right-prep"],
        ["LinkedIn Recruiting Course", "https://www.linkedin.com/learning/recruiting-foundations"],
        ["People Analytics (Coursera)", "https://www.coursera.org/learn/wharton-people-analytics"],
        ["Udemy HR Business Partner Course", "https://www.udemy.com/course/hr-as-strategic-business-partner"]
    ],
    "Game Developer": [
        ["Unity Learn Pathway", "https://learn.unity.com/pathway/game-development"],
        ["Unreal Engine Online Learning", "https://www.unrealengine.com/en-US/onlinelearning-courses"],
        ["CS50 Game Development", "https://www.edx.org/course/cs50s-introduction-to-game-development"],
        ["C# for Unity (Coursera)", "https://www.coursera.org/learn/programming-unity-game-development"],
        ["GameDev.tv Courses", "https://www.udemy.com/user/gamedev-tm"]
    ],
    "Graphic Designer": [
        ["Adobe Creative Cloud Tutorials", "https://helpx.adobe.com/creative-cloud/tutorials.html"],
        ["Canva Design School", "https://www.canva.com/learn/design-school/"],
        ["Graphic Design Specialization (Coursera)", "https://www.coursera.org/specializations/graphic-design"],
        ["Visual Design (LinkedIn)", "https://www.linkedin.com/learning/visual-design-foundations"],
        ["Envato Tuts+ Graphic Design", "https://tutsplus.com"]
    ],
}

# Mapping of alternative/synonym roles to main keys in COURSE_RECOMMENDATIONS
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
    "pm": "product manager",
    "ba": "business analyst",
    "business analysis": "business analyst",
    "cybersecurity": "cybersecurity specialist",
    "cyber security": "cybersecurity specialist",
    "security analyst": "cybersecurity specialist",
    "ai researcher": "ai researcher",
    "ai engineer": "ai researcher",
    "artificial intelligence": "ai researcher",
    "data analyst": "data analyst",
    "data analysis": "data analyst",
    "data scientist": "data scientist",
    "data engineer": "data engineer",
    "etl developer": "data engineer",
    "pipeline engineer": "data engineer",
    "qa": "quality assurance engineer",
    "qa tester": "quality assurance engineer",
    "qa engineer": "quality assurance engineer",
    "software tester": "quality assurance engineer",
    "manual tester": "quality assurance engineer",
    "automation tester": "quality assurance engineer",
    "graphic designer": "graphic designer",
    "visual designer": "graphic designer",
    "game dev": "game developer",
    "unity dev": "game developer",
    "unreal dev": "game developer",
    "technical writer": "technical writer",
    "tech writer": "technical writer",
    "documentation specialist": "technical writer",
    "content writer": "content writer",
    "copywriter": "content writer",
    "seo writer": "content writer",
    "digital marketer": "digital marketer",
    "marketing specialist": "digital marketer",
    "seo specialist": "digital marketer",
    "sem specialist": "digital marketer",
    "hr": "hr specialist",
    "human resources": "hr specialist",
    "recruiter": "hr specialist",
    "talent acquisition": "hr specialist",
    "finance analyst": "finance analyst",
    "financial analyst": "finance analyst",
    "support engineer": "technical support engineer",
    "tech support": "technical support engineer",
    "it support": "technical support engineer"
}

def render_resources():
    st.markdown("""
        <style>
            .section-header {
                font-size: 24px;
                font-weight: bold;
                color: #004080;
                margin-bottom: 10px;
            }
            .course-link {
                background-color: #e3f2fd;
                padding: 10px;
                border-radius: 10px;
                margin: 5px 0;
                font-size: 16px;
            }
            .back-button {
                margin-top: 30px;
                text-align: center;
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

    role = st.session_state.get("selected_role", "").lower().strip()
    resolved_key = None

    if role in COURSE_RECOMMENDATIONS:
        resolved_key = role
    else:
        for alias, mapped_key in ROLE_ALIASES.items():
            if alias in role:
                resolved_key = mapped_key
                break

    st.markdown("<div class='section-header'>🎓 Recommended Courses & Certifications</div>", unsafe_allow_html=True)

    if resolved_key and resolved_key in COURSE_RECOMMENDATIONS:
        for course in COURSE_RECOMMENDATIONS[resolved_key]:
            st.markdown(f"<div class='course-link'>🔗 <a href='{course[1]}' target='_blank'>{course[0]}</a></div>", unsafe_allow_html=True)
    else:
        st.info("No course recommendations available for this role yet.")

    with st.container():
        st.markdown("<div class='back-button'>", unsafe_allow_html=True)
        if st.button("🔙 Back to Dashboard"):
            st.session_state.selected_module = None
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
