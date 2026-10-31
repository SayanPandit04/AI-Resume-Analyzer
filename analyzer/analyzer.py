def analyze_resume(skills):

    strengths = []
    suggestions = []

    if len(skills) >= 3:
        strengths.append("Good variety of skills")
    else:
        suggestions.append("Add more technical skills")

    if "communication" in skills:
        strengths.append("Good communication skill")

    if "python" not in skills:
        suggestions.append("Learn Python")

    if "sql" not in skills:
        suggestions.append("Learn SQL")

    return strengths, suggestions