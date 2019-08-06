from django.urls import re_path, include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^argent/', include('argent.urls')),
    re_path(r'^comments/', include('comments.urls'), name='comments'),
    re_path(r'^account/', include('accounts.urls')),
    # Posts Links
    re_path(r'^posts/', TemplateView.as_view(template_name='posts/react.html'),
            name='posts-list'),
    path('walking', TemplateView.as_view(template_name='posts/walking.html')),
    path('api/posts/', include('posts.urls')),
    # Scraper Links
    re_path(r'^scrape/', TemplateView.as_view(template_name='scrape/react.html'),
            name='scrape-list'),
    path('walking', TemplateView.as_view(template_name='scrape/walking.html')),
    path('api/scrape/', include('scrape.urls')),
    # Homepage Link
    re_path(r'^', include('home.urls'), name='home')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
