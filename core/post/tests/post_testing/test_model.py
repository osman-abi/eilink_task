"""In this file we are testing model"""
from django.urls import reverse

# pylint: disable=import-error
from core.post.serializers_post import PostSerializer
from post.models import Post
import test_setup


class TestPostModel(test_setup.TestSetUp):
    """This class is used for testing the cases"""

    def access_token(self):
        """This function is used for get access token easily from another functions"""

        register_url = reverse("register")
        register_data = {
            "email": "test@email1.com",
            "username": "testusername1",
            "password": "test_password1",
        }

        response = self.client.post(register_url, register_data, format="json")
        return response.json().get("access_token")

    def user_can_get_all_posts(self):
        """In this case we're checking that user can get all post"""
        response = self.client.get(self.get_all_posts_url)
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

    def user_can_create_post(self):
        """In this case we're checking that user can create post with authorization"""
        response = self.client.post(
            self.post_create_url,
            self.post_data,
            format="json",
            **{"HTTP_AUTHORIZATION": f"Bearer {self.access_token()}"},
        )

        self.assertEqual(response.status_code, 201)

    def user_can_update_post(self):
        """In this case we're checking that user can update post with authorization"""
        response = self.client.put(
            self.post_update_url,
            self.updated_post_data,
            format="json",
            **{"HTTP_AUTHORIZATION": f"Bearer {self.access_token()}"},
        )
        self.assertEqual(response.status_code, 200)

    def user_can_get_post_detail(self):
        """In this case we're checking that user can retrieve the post"""
        response = self.client.get(self.post_detail_url)

        self.assertEqual(response.status_code, 200)

    def user_can_upvote_post(self):
        """In this case we're checking that user can upvote post with authorization"""
        response = self.client.post(
            self.post_upvote_url,
            **{"HTTP_AUTHORIZATION": f"Bearer {self.access_token()}"},
        )
        self.assertEqual(response.status_code, 200)

    def user_can_delete_post(self):
        """In this case we're checking that user can delete post with authorization"""
        response = self.client.delete(
            self.post_delete_url,
            **{"HTTP_AUTHORIZATION": f"Bearer {self.access_token()}"},
        )
        self.assertEqual(response.status_code, 204)
