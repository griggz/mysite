from django.conf.urls import url

from home.views import HomeView
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

app_name = 'home'

urlpatterns = [
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^$', HomeView.as_view(), name='landing')


]

