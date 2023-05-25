from django.urls import path

from . import views

app_name = "conversation"

urlpatterns = [
    path("new/<int:pk>/", views.new_conversation, name="new_conversation"),
    path(
        "send/<int:conversation_pk>/", views.send_message, name="send_message"
    ),
    path("<int:pk>/", views.new_conversation, name="conversation_detail"),
]
