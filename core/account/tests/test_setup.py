"""This file is a setup file for preparing test"""
from rest_framework.test import APITestCase
from django.urls import reverse
# pylint: disable=W0235

class TestSetUp(APITestCase):
    """We inherit from APITestCase to build setup"""
    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse("login")

        self.register_data = {
            "email": "test@email.com",
            "username": "testusername",
            "password": "test_password",
        }

        self.login_data = {"email": "test@email.com", "password": "test_password"}

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
