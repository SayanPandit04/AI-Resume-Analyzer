
import re


def extract_skills(text):

    skills_db = [
        "python",
        "django",
        "flask",
        "sql",
        "sqlite",
        "mysql",
        "html",
        "css",
        "javascript",
        "java",
        "c++",
        "c",
        "pandas",
        "scikit-learn",
        "jupyter",
        "github",
        "git",
        "api",
        "oop",
        "dsa",
        "dbms",
        "communication",
        "management",
        "team work",
    ]

    found_skills = []

    text = text.lower()

    for skill in skills_db:

        if skill == "c":
            pattern = r'(?<![a-z0-9])c(?![a-z0-9]|\+\+)'
        else:
            pattern = r'(?<![a-z0-9])' + re.escape(skill) + r'(?![a-z0-9])'

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills


def get_strengths(skills):

    strengths = []

    technical_skills = [
        "python", "django", "flask", "sql", "sqlite",
        "mysql", "html", "css", "javascript", "java",
        "c", "c++", "pandas", "scikit-learn",
        "jupyter", "api", "oop", "dsa", "dbms"
    ]

    technical_count = sum(
        1 for skill in skills if skill in technical_skills
    )

    if technical_count >= 5:
        strengths.append("Strong technical skill set")

    if "python" in skills:
        strengths.append("Good Python knowledge")

    if any(skill in skills for skill in ["sql", "sqlite", "mysql"]):
        strengths.append("Database knowledge")

    if "html" in skills and "css" in skills:
        strengths.append("Web development knowledge")

    if "django" in skills:
        strengths.append("Django development knowledge")

    if "javascript" in skills:
        strengths.append("JavaScript knowledge")

    return strengths


def get_suggestions(skills):

    suggestions = []

    if "django" not in skills:
        suggestions.append("Learn Django for Python web development")

    if "javascript" not in skills:
        suggestions.append("Improve JavaScript skills for frontend development")

    if "java" not in skills:
        suggestions.append("Learn Java for broader programming knowledge")

    if not any(skill in skills for skill in ["sql", "sqlite", "mysql"]):
        suggestions.append("Improve SQL and database skills")

    if "git" not in skills and "github" not in skills:
        suggestions.append("Practice Git and GitHub")

    if "communication" not in skills:
        suggestions.append("Improve communication skills")

    return suggestions


def calculate_score(text):

    text = text.lower()

    score = 0

    # Skills - 40 marks
    skills = [
        "python",
        "sql",
        "sqlite",
        "django",
        "html",
        "css",
        "javascript",
        "java",
        "c"
    ]

    detected_skills = extract_skills(text)

    skill_count = 0

    for skill in skills:
        if skill in detected_skills:
            skill_count += 1

    score += min(skill_count * 5, 40)

    # Experience - 20 marks
    if "experience" in text or "intern" in text:
        score += 20

    # Projects - 20 marks
    if "projects" in text or "project" in text:
        score += 20

    # Education - 10 marks
    if "education" in text or "b.tech" in text:
        score += 10

    # Certification - 10 marks
    if "certification" in text or "certificate" in text:
        score += 10

    return score


def check_sections(text):

    text = text.lower()

    sections = {
        "Education": False,
        "Experience": False,
        "Internships": False,
        "Projects": False,
        "Skills": False,
        "Certifications": False,
        "Career Objective": False
    }

    if "education" in text:
        sections["Education"] = True

    if "experience" in text:
        sections["Experience"] = True

    if "internship" in text or "intern" in text:
        sections["Internships"] = True

    if "projects" in text or "project" in text:
        sections["Projects"] = True

    if "skills" in text:
        sections["Skills"] = True

    if "certification" in text or "certificate" in text:
        sections["Certifications"] = True

    if "career objective" in text or "objective" in text or "profile" in text:
        sections["Career Objective"] = True

    return sections
