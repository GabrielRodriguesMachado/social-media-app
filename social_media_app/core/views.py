from django.shortcuts import render, redirect
from django.db.models import Count
from django.core.paginator import Paginator

from post.models import Post
from dashboard.models import Follow
from .forms import SignupForm

from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    user = request.user

    following_users = Follow.objects.filter(follower=user).values_list(
        "following", flat=True
    )
    all_posts = (
        Post.objects.exclude(created_by=user)
        .filter(created_by__in=following_users)
        .annotate(comment_count=Count("comments"))
        .order_by("-date_posted")
    )

    paginator = Paginator(all_posts, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    for post in page_obj:
        post.like_count = post.likes.count()
        post.has_liked = post.likes.filter(user=user).exists()

    return render(request, "core/index.html", {"posts": page_obj})


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
