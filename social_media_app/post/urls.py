from django.urls import path

from . import views


app_name = "post"

urlpatterns = [
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/add_comment/", views.add_comment, name="add_comment"),
]
