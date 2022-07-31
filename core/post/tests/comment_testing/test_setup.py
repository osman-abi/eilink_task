"""This file is a setup file for preparing test"""
from rest_framework.test import APITestCase
from django.urls import reverse
# pylint: disable=import-error
from post.models import Comment, Post
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
        # At this point we create test comment for retrieve comment detail info
        self.created_test_comment = Comment.objects.create(
            author_id=self.user.id,
            post_id=self.created_test_post.id,
            content="test content",
        )

        self.get_comment_list_url = reverse("comment-list")
        self.comment_create_url = reverse("comment-create")
        self.comment_update_url = reverse(
            "comment-update", kwargs={"pk": self.created_test_comment.pk}
        )
        self.comment_delete_url = reverse(
            "comment-delete", kwargs={"pk": self.created_test_comment.pk}
        )

        self.comment_data = {
            "post": self.created_test_post.id,
            "content": "test content",
        }

        self.reply_comment_data = {
            "post": self.created_test_post.id,
            "content": "test content",
            "parent": self.created_test_comment.id,
        }

        self.update_comment_data = {"content": "updated comment"}

        return super().setUp()

    def tearDown(self):
        # pylint: disable=useless-super-delegation
        return super().tearDown()
