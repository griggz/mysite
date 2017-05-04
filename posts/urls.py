from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^$', views.posts_list, name='list'),
    url(r'^create/$', views.posts_create, name='create'),
    url(r'^detail/(?P<id>[0-9]+)/$', views.posts_detail, name='detail'),
    url(r'^update/$', views.posts_update, name='update'),
    url(r'^delete/$', views.posts_delete, name='delete'),

]
