from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User

from post.models import Post
from .models import Follow


@login_required
def index(request):
    posts = Post.objects.filter(created_by=request.user).all()

    following_users = User.objects.filter(
        followers__follower=request.user
    ).values("id", "username")

    return render(
        request,
        "dashboard/index.html",
        {
            "posts": posts,
            "following": following_users,
            "is_following": "my_profile",
        },
    )


@login_required
def logout_view(request):
    logout(request)

    return redirect("core:index")


@login_required
def follow_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    follow, created = Follow.objects.get_or_create(
        follower=request.user, following=user
    )
    posts, following_users, is_following = common_operations(
        request.user, user
    )

    return render(
        request,
        "dashboard/index.html",
        {
            "posts": posts,
            "user": user,
            "following": following_users,
            "is_following": is_following,
        },
    )


@login_required
def unfollow_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    Follow.objects.filter(follower=request.user, following=user).delete()
    posts, following_users, is_following = common_operations(
        request.user, user
    )

    return render(
        request,
        "dashboard/index.html",
        {
            "posts": posts,
            "user": user,
            "following": following_users,
            "is_following": is_following,
        },
    )


@login_required
def profile_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    posts, following_users, is_following = common_operations(
        request.user, user
    )

    return render(
        request,
        "dashboard/index.html",
        {
            "posts": posts,
            "user": user,
            "following": following_users,
            "is_following": is_following,
        },
    )


def common_operations(current_user, target_user):
    posts = Post.objects.filter(created_by=target_user).all()[::-1]
    following_users = User.objects.filter(
        followers__follower=target_user.id
    ).values("id", "username")
    is_following = User.objects.filter(
        followers__follower=current_user, id=target_user.id
    ).exists()

    return posts, following_users, is_following
