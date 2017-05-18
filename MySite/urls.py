from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
# from django.contrib.auth import views as auth_views
from accounts.views import (login_view, register_view, logout_view)
from home.views import HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^argent/', include('argent.urls'), name='argent'),
    url(r'^posts/', include('posts.urls'), name='posts'),
    url(r'^comments/', include('comments.urls'), name='comments'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^register/$', register_view, name='register'),
    url(r'^', include('home.urls'), name='home'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
