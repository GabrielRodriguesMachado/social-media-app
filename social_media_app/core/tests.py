from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from post.models import Post


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpassword",
        )
        self.post = Post.objects.create(
            created_by=self.user, content="Test content"
        )

    def test_str_representation(self):
        self.assertEqual(
            str(self.post),
            f"Posted by {self.user.username}",
        )


class PostViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpassword",
        )
        self.post = Post.objects.create(
            created_by=self.user, content="Test content"
        )

    def test_contact_view(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/contact.html")
