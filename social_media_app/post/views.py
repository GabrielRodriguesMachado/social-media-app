from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib.auth.models import User

from .models import Post
from .forms import CommentForm, PostForm


@login_required
def posts(request):
    query = request.GET.get("query", "")
    posts = Post.objects.annotate(comment_count=Count("comments")).all()[::-1]
    users = (
        User.objects.filter(username__icontains=query)
        .exclude(id=request.user.id)
        .all()
    )

    if query:
        posts = [post for post in posts if query in post.content]

    return render(
        request,
        "post/posts.html",
        {"posts": posts, "query": query, "users": users},
    )


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
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
