from django.urls import re_path
from . import views

app_name = 'scrape'

urlpatterns = [
    re_path(r'^create/$', views.create_scrape, name='create'),
    re_path(r'^results/(?P<slug>[\w-]+)/$', views.scrape_details_list, name='results')
    ]