from django.views.generic import View
from django.shortcuts import render, get_object_or_404, redirect
from .forms import FeedbackForm, AboutMeForm
from django.contrib import messages
from .models import About
from posts.models import new_posts
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


class HomeView(View):

    def get(self, request, *args, **kwargs):
        context = {
            "new_posts": new_posts()
        }
        return render(request, "home/home.html", context)


def feedback(request):
    form = FeedbackForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        user_feedback = form.cleaned_data.get("comments")
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()

        # Email Admin
        from_email = settings.EMAIL_HOST_USER
        send_mail(
            'Feedback Submitted!',
            user_feedback,
            from_email,
            ['wayne@vvayne.co'],
            fail_silently=False,
        )

        messages.success(request, "Your feedback has been submitted!")
        return redirect('home:landing')
    context = {
        "title": "Feedback",
        "form": form,
    }
    return render(request, "home/feedback_form.html", context)


def about(request):
    form = AboutMeForm(request.POST or None, request.FILES or None)
    qs = About.objects.filter(id=1)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('home:landing')
    context = {
        "object_list": qs,
        "title": "About Me"
    }
    return render(request, "home/about_me.html", context)


def under_construction(request):
    return render(request, "home/under_construction.html")


