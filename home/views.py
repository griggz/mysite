from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


# Create your views here.

# def index(request):
#     return render(request, 'base/Home.html')

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/home.html", {})
