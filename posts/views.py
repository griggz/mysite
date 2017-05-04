from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


# Create your views here.

def posts_list(request):
    queryset = Post.objects.all()
    context = {
            "object_list": queryset,
            "title": "List"
        }

    return render(request, 'posts/index.html', context)


def posts_create(request):
    return HttpResponse("<h1>HELLO</h1>")


def posts_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance
    }
    return render(request, 'posts/detail.html', context)


def posts_update(request):
    return HttpResponse("<h1>Update</h1>")


def posts_delete(request):
    return HttpResponse("<h1>Delete</h1>")
