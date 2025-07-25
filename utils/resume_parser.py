import re
import pdfplumber
from docx import Document

def parse_resume(file_path):
    raw_text = ""
    num_pages = 0

    # Extract text based on file type
    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            num_pages = len(pdf.pages)
            for page in pdf.pages:
                raw_text += page.extract_text() + "\n"
    elif file_path.endswith(".docx"):
        doc = Document(file_path)
        raw_text = "\n".join([para.text for para in doc.paragraphs])
        num_pages = "1 (DOCX)"

    # Extract email
    email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', raw_text)
    email = email_match.group(0) if email_match else "N/A"

    # Extract phone
    phone_match = re.search(r'(\+91[-\s]?)?[6-9]\d{9}', raw_text)
    phone = phone_match.group(0) if phone_match else "N/A"

    # Extract LinkedIn
    linkedin_match = re.search(r'https?://(www\.)?linkedin\.com/in/[A-Za-z0-9\-_/]+', raw_text)
    linkedin = linkedin_match.group(0) if linkedin_match else "N/A"

    # Extract GitHub
    github_match = re.search(r'https?://(www\.)?github\.com/[A-Za-z0-9\-_/]+', raw_text)
    github = github_match.group(0) if github_match else "N/A"

    # Name extraction
    lines = raw_text.strip().split('\n')[:5]
    name = "N/A"
    for line in lines:
        if email not in line and not re.search(r'\d{10}', line) and "@" not in line:
            possible_name = re.sub(r'[^A-Za-z\s]', '', line).strip()
            if len(possible_name.split()) >= 2:
                name = possible_name
                break

    # Extract skills (keyword matching)
    common_skills = [
        "python", "java", "c++", "sql", "html", "css", "javascript",
        "machine learning", "deep learning", "pandas", "numpy",
        "tensorflow", "keras", "scikit-learn", "flask", "django",
        "react", "node", "git", "github", "linux", "excel", "power bi"
    ]

    found_skills = []
    for skill in common_skills:
        if re.search(rf'\b{re.escape(skill)}\b', raw_text, re.IGNORECASE):
            found_skills.append(skill.title())

    found_skills = sorted(list(set(found_skills)))  # Deduplicate + sort

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "linkedin": linkedin,
        "github": github,
        "num_pages": num_pages,
        "text": raw_text,
        "raw_text": raw_text,
        "skills": found_skills
    }
