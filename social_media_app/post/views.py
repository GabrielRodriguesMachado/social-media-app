from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from .models import Post
from .forms import CommentForm, PostForm


@login_required
def posts(request):
    query = request.GET.get("query", "")
    user = request.user

    all_posts = Post.objects.annotate(
        comment_count=Count("comments")
    ).order_by("-date_posted")

    users = (
        User.objects.filter(username__icontains=query)
        .exclude(id=user.id)
        .all()
    )

    if query:
        all_posts = all_posts.filter(content__icontains=query)

    paginator = Paginator(all_posts, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    for post in page_obj:
        post.like_count = post.likes.count()
        post.has_liked = post.likes.filter(user=user).exists()

    return render(
        request,
        "post/posts.html",
        {"posts": page_obj, "query": query, "users": users},
    )


@login_required
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    post.like_count = post.likes.count()
    post.has_liked = post.likes.filter(user=request.user).exists()

    return render(
        request, "post/detail.html", {"post": post, "comments": comments}
    )


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect("post:detail", pk=post.pk)
    else:
        form = CommentForm()

    return redirect("post:detail", pk=post.pk)


@login_required
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)

            post.created_by = request.user
            post.save()

            return redirect("post:detail", pk=post.pk)
    else:
        form = PostForm()

    return render(request, "post/new_post.html", {"form": form})


@login_required
def delete_post(request, pk):
    item = get_object_or_404(Post, pk=pk, created_by=request.user)
    item.delete()

    return redirect("dashboard:index")


@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk, created_by=request.user)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post.save()

            return redirect("post:detail", pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(
        request, "post/new_post.html", {"form": form, "title": "Edit Post"}
    )


@login_required
def like_post(request, pk, action):
    post = get_object_or_404(Post, pk=pk)
    post.likes.get_or_create(user=request.user)

    if action == "detail":
        return redirect("post:detail", pk=post.pk)
    elif action == "posts":
        return redirect("post:posts")
    elif action == "dashboard":
        return redirect("dashboard:index")
    elif action == "profile":
        return redirect("dashboard:profile", user_id=post.created_by.id)
    else:
        return redirect("core:index")


@login_required
def unlike_post(request, pk, action):
    post = get_object_or_404(Post, pk=pk)
    post.likes.filter(user=request.user).delete()

    if action == "detail":
        return redirect("post:detail", pk=post.pk)
    elif action == "posts":
        return redirect("post:posts")
    elif action == "dashboard":
        return redirect("dashboard:index")
    elif action == "profile":
        return redirect("dashboard:profile", user_id=post.created_by.id)
    else:
        return redirect("core:index")
