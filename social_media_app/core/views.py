from django.shortcuts import render
from django.db.models import Count
from post.models import Post


def index(request):
    posts = Post.objects.annotate(comment_count=Count("comments")).all()[:10]

    return render(request, "core/index.html", {"posts": posts})


def contact(request):
    return render(request, "core/contact.html")
