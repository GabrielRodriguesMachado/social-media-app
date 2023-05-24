from django.shortcuts import render

from post.models import Post


def index(request):
    posts = Post.objects.all()[:10]
    return render(request, "core/index.html", {"posts": posts})


def contact(request):
    return render(request, "core/contact.html")
