from django.shortcuts import render
from furry_funnies.utils import get_author_obj, get_all_posts_obj


def index(request):
    author = get_author_obj()
    context = {
        "author": author
    }
    return render(request, template_name="index.html", context=context)


def dashboard(request):
    author = get_author_obj()
    posts = get_all_posts_obj()
    context = {
        "author": author,
        "posts": posts,
    }
    return render(request, template_name="dashboard.html", context=context)
