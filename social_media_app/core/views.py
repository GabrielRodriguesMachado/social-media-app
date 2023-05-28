from django.shortcuts import render, redirect
from django.db.models import Count

from post.models import Post
from dashboard.models import Follow
from .forms import SignupForm

from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    user = request.user

    if user.is_authenticated:
        following_users = Follow.objects.filter(follower=user).values_list(
            "following", flat=True
        )
        posts = (
            Post.objects.exclude(created_by=user)
            .filter(created_by__in=following_users)
            .annotate(comment_count=Count("comments"))
            .all()[:10:-1]
        )
    else:
        posts = Post.objects.annotate(comment_count=Count("comments")).all()[
            :10:-1
        ]

    return render(request, "core/index.html", {"posts": posts})


def contact(request):
    return render(request, "core/contact.html")


def about(request):
    return render(request, "core/about.html")


def privacy_policy(request):
    return render(request, "core/privacy_policy.html")


def terms_of_use(request):
    return render(request, "core/terms_of_use.html")


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("/login/")
    else:
        form = SignupForm()

    return render(request, "core/signup.html", {"form": form})
