from django.urls import re_path, path
from . import views
from django.views.generic import TemplateView

app_name = 'posts-api'

urlpatterns = [
    # re_path(r'^$', views.posts_list, name='list'),
    # re_path(r'^create/$', views.posts_create, name='create'),
    # re_path(r'^detail/(?P<slug>[\w-]+)/$', views.posts_detail, name='detail'),
    # re_path(r'^(?P<slug>[\w-]+)/edit/$', views.posts_update, name='update'),
    # re_path(r'^(?P<slug>[\w-]+)/delete/$', views.posts_delete, name='delete'),
    # REACT URLS
    # re_path(r'^react/',
    #         TemplateView.as_view(template_name='posts/react.html')),
    path('', views.PostListCreateAPIView.as_view(), name='list-create'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.PostDetailAPIView.as_view(),
            name='detail'),
]



