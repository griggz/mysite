from django import forms
from .models import Feedback, About
from django.forms import TextInput, Textarea


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        widgets = {'comments': Textarea(attrs={'placeholder': 'Enter Your Comments'})}
        labels = {'comments': ''}
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
