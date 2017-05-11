from django import forms
from .models import Feedback, About


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            "comments",
        ]


class AboutMeForm(forms.ModelForm):
    class Meta:
        model = About
        fields = [
            "user",
            "content"
        ]
