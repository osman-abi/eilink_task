"""This file is used for testing the model"""
from django.urls import reverse
import test_setup


class TestCommentModel(test_setup.TestSetUp):
    """This class is used for testing the cases"""
    def access_token(self):
        """This function is used for get access token easily from another functions"""

        register_url = reverse("register")
        register_data = {
            "email": "test@email2.com",
            "username": "testusername2",
            "password": "test_password2",
        }

        response = self.client.post(register_url, register_data, format="json")
        return response.json().get("access_token")

    def user_can_comment(self):
        """In this case we're checking that the user can comment with authorization"""
        reponse = self.client.post(
            self.comment_create_url,
            self.comment_data,
            format="json",
            **{"HTTP_AUTHORIZATION": f"Bearer {self.access_token()}"},
        )

        self.assertEqual(reponse.status_code, 201)

    def user_can_delete_comment(self):
        """In this case we're checking that the user can delete comment with authorization"""
        response = self.client.delete(
            self.comment_delete_url,
            **{"HTTP_AUTHORIZATION": f"Bearer {self.access_token()}"},
        )

        self.assertEqual(response.status_code, 204)

    def get_all_comments(self):
        """In this case we're checking that the user can get all comment """
        response = self.client.get(self.get_comment_list_url)

        self.assertEqual(response.status_code, 200)

    def user_can_update_comment(self):
        """In this case we're checking that the user can update comment with authorization"""

        response = self.client.put(
            self.comment_update_url,
            self.update_comment_data,
            format="json",
            **{"HTTP_AUTHORIZATION": f"Bearer {self.access_token()}"},
        )

        self.assertEqual(response.status_code, 200)
