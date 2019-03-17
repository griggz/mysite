from django.urls import path, re_path, include
from home.views import HomeView
from . import views
# from django.contrib import admin
# from django.contrib.auth import views as auth_views

app_name = 'home'

urlpatterns = [
    re_path(r'^feedback/$', views.feedback, name='feedback'),
    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^under_construction/$', views.under_construction, name='under_construction'),
    re_path(r'^$', HomeView.as_view(), name='landing')
]
