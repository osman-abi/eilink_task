"""This file is setup file for testing"""
from rest_framework.test import APITestCase
from django.urls import reverse
# pylint: disable=import-error
from post.models import Post
from account.models import User


class TestSetUp(APITestCase):
    """We inherit from APITestCase to build setup"""

    # pylint: disable=too-many-instance-attributes
    def setUp(self):
        # We create user for create test object
        self.user = User.objects.create(
            email="test@email.com", username="testusername", password="test_password"
        )
        # At this point we create test object for retrieve detail data
        self.created_test_post = Post.objects.create(
            author_id=self.user.id, title="test"
        )

        self.get_all_posts_url = reverse("post-list")
        self.post_create_url = reverse("post-create")
        self.post_detail_url = reverse(
            "post-detail", kwargs={"pk": self.created_test_post.pk}
        )
        self.post_update_url = reverse(
            "post-update", kwargs={"pk": self.created_test_post.pk}
        )
        self.post_delete_url = reverse(
            "post-delete", kwargs={"pk": self.created_test_post.pk}
        )
        self.post_upvote_url = reverse(
            "upvote", kwargs={"pk": self.created_test_post.pk}
        )

        self.post_data = {"title": "test title"}

        self.updated_post_data = {"title": "updated post title"}

        return super().setUp()

    def tearDown(self):
        # pylint: disable=useless-super-delegation
        return super().tearDown()
