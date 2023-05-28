from django.urls import path

from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.index, name="index"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/<int:user_id>/", views.profile_view, name="profile"),
    path("follow/<int:user_id>/", views.follow_user, name="follow"),
    path("unfollow/<int:user_id>/", views.unfollow_user, name="unfollow"),
]
