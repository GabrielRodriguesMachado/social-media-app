from django.urls import path

from . import views


app_name = "post"

urlpatterns = [
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/add_comment/", views.add_comment, name="add_comment"),
    path("new_post/", views.new_post, name="new_post"),
    path("<int:pk>/delete_post/", views.delete_post, name="delete_post"),
]
