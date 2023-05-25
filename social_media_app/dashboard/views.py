from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect

from post.models import Post


@login_required
def index(request):
    posts = Post.objects.filter(created_by=request.user).all()

    return render(request, "dashboard/index.html", {"posts": posts})


@login_required
def logout_view(request):
    logout(request)

    return redirect("core:index")
