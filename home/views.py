from django.views.generic import View
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import FeedbackForm, AboutMeForm
from django.contrib import messages
from .models import About
import datetime
from posts.models import new_posts
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
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Your Feedback has been sent!")
        return redirect('home:landing')
    context = {
        "title": "New Feedback",
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


def resume(request):
    pdf = ''

    return render(request, "home/resume.html")

