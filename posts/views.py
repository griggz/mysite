from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def posts_list(request):
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 3)  # Show 25 posts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
            "object_list": queryset,
            "title": "",
            "page_request_var": page_request_var,
        }

    return render(request, 'posts/post-list.html', context)


def posts_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, "Your Post has been created!")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": "New Post",
        "form": form,
    }
    return render(request, "posts/post_form.html", context)


def posts_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, 'posts/detail.html', context)


def posts_update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Your changes have been saved!")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": "Edit Post",
        "instance": instance,
        "form": form,
    }
    return render(request, 'posts/post_form.html', context)


def posts_delete(request, id=None):
    if not request.user.is_staff or request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Post Successfully Deleted")
    return redirect("posts:list")
