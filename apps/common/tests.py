from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIClient


# Create your tests here.


class TestCommon(TestCase):
    fixtures = ["users"]

    def setUp(self) -> None:
        self.client = APIClient()
        # check data in fixture json file
        self.test_user1 = User.objects.get(email="user1@email.com")

    def test_health_view(self):
        response = self.client.get(reverse("health_view"))
        self.assertEqual(response.status_code, 200)

    def test_protected_view(self):
        self.client.force_authenticate(user=self.test_user1)
        response = self.client.get(reverse("protected_view"))
        self.assertEqual(response.status_code, 200)
