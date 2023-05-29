from django.test import TestCase
from django.contrib.auth.models import User

from .models import Follow


class FollowModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username="testuser1",
            email="test1@example.com",
            password="testpassword1",
        )
        self.user2 = User.objects.create_user(
            username="testuser2",
            email="test2@example.com",
            password="testpassword2",
        )
        self.follow = Follow.objects.create(
            follower=self.user1, following=self.user2
        )

    def test_str_representation(self):
        self.assertEqual(
            str(self.follow),
            f"{self.user1} follows {self.user2}",
        )

    def test_follower_field(self):
        self.assertEqual(self.follow.follower, self.user1)

    def test_following_field(self):
        self.assertEqual(self.follow.following, self.user2)

    def test_created_at_field(self):
        self.assertIsNotNone(self.follow.created_at)
