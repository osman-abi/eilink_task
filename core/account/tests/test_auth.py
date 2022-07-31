"""This file is used for testing the model"""
from .test_setup import TestSetUp


class TestAuthModel(TestSetUp):
    """This class is used for testing the cases"""

    def test_user_cannot_register_with_no_data(self):
        """this case is used for the user cannot register without data"""

        response = self.client.post(self.register_url)
        # At this point we're checking that the response's status equals 400
        self.assertEqual(response.status_code, 400)

    def test_user_can_register_with_full_data(self):
        """this case is used for the user can register with full data"""

        response = self.client.post(
            self.register_url, self.register_data, format="json"
        )

        # At this point we're checking that the response's status equals to 200
        self.assertEqual(response.status_code, 200)

    def access_token(self):
        """We create this function for get access token in another function"""

        response = self.client.post(
            self.register_url, self.register_data, format="json"
        )

        return response.json().get("access_token")

    def test_user_cannot_login_without_access_token(self):
        """User cannot login without authorization"""

        response = self.client.post(self.login_url, self.login_data, format="json")
        # At this point we're checking that the user is authorized or not
        self.assertEqual(response.status_code, 401)

    def test_user_can_login_with_full_data(self):
        """User cannot login with authorization"""

        response = self.client.post(
            self.login_url,
            self.login_data,
            format="json",
            **{"HTTP_AUTHORIZATION": f"Bearer {self.access_token()}"},
        )

        self.assertEqual(response.status_code, 201)
