from django.urls import path

from . import views


app_name = "post"

urlpatterns = [
    path("", views.posts, name="posts"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/add_comment/", views.add_comment, name="add_comment"),
    path("new_post/", views.new_post, name="new_post"),
    path("<int:pk>/delete_post/", views.delete_post, name="delete_post"),
    path("<int:pk>/edit_post/", views.edit_post, name="edit_post"),
]
