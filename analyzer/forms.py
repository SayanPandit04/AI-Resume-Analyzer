
from django import forms
from .models import Resume


class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = ('name', 'resume')

    def clean_resume(self):
        resume = self.cleaned_data.get('resume')

        if resume and not resume.name.lower().endswith('.pdf'):
            raise forms.ValidationError("Only PDF files are allowed.")

        return resume
