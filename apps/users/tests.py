from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient


class TestUsers(TestCase):
    fixtures = ["users"]

    def setUp(self) -> None:
        self.client = APIClient()
        # check data in fixture json file
        self.test_user1 = User.objects.get(email="user1@email.com")

    def test_register(self) -> None:
        response = self.client.post(
            reverse("token_register"),
            {
                "first_name": "firstname2",
                "last_name": "lastname2",
                "username": "username2",
                "password": "testpwd2",
            },
        )
        self.assertEqual(response.status_code, 200)
