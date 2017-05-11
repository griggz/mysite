from django.views.generic import View
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Feedback
from .forms import FeedbackForm
from django.contrib import messages

# Create your views here.


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/home.html", {})


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
