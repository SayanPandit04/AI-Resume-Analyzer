from django.shortcuts import render
from .forms import ResumeForm
from .resume_parser import extract_text
from .skill_detector import (
    extract_skills,
    get_strengths,
    get_suggestions,
    calculate_score,
    check_sections
)

def upload_resume(request):

    form = ResumeForm()

    if request.method == "POST":

        form = ResumeForm(request.POST, request.FILES)

        if form.is_valid():

            resume_obj = form.save()

            text = extract_text(resume_obj.resume.path)
            skills = extract_skills(text)
            strengths = get_strengths(skills)
            suggestions = get_suggestions(skills)
            score = calculate_score(text)
            sections = check_sections(text)

            return render(
                request,
                "analyzer/result.html",
                {"text": text,
                "skills": skills,
                "strengths": strengths,
                "suggestions": suggestions,
                "score": score,
                "sections": sections,
                }
            )

    return render(
        request,
        "analyzer/upload.html",
        {"form": form}
    )