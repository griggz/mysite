from django.urls import re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^argent/', include('argent.urls')),
    re_path(r'^posts/', include('posts.urls')),
    re_path(r'^scrape/', include('scrape.urls')),
    re_path(r'^comments/', include('comments.urls'), name='comments'),
    re_path(r'^account/', include('accounts.urls')),
    re_path(r'^', include('home.urls'), name='home'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
