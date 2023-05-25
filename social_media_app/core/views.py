from django.shortcuts import render, redirect
from django.db.models import Count
from post.models import Post

from .forms import SignupForm


def index(request):
    posts = Post.objects.annotate(comment_count=Count("comments")).all()[
        :10:-1
    ]

    return render(request, "core/index.html", {"posts": posts})


def contact(request):
    return render(request, "core/contact.html")


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("/login/")
    else:
        form = SignupForm()

    return render(request, "core/signup.html", {"form": form})
