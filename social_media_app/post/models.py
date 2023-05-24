from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    created_by = models.ForeignKey(
        User, related_name="posts", on_delete=models.CASCADE
    )
    content = models.TextField()
    image = models.ImageField(upload_to="post_images", blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Posted by {self.created_by.username}"
