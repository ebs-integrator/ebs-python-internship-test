from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


# Create your tests here.


class BlogTests(TestCase):
    fixtures = ["users", "blogs", "categories"]

    def setUp(self) -> None:
        self.client = APIClient()
        # Get test user from bd and set it as authenticated user
        user = User.objects.get(email="user1@email.com")
        self.client.force_authenticate(user=user)

    def test_retrieve(self):
        response = self.client.get(reverse("blog_item", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list(self):
        response = self.client.get(reverse("blog_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class CategoryTests(TestCase):
    fixtures = ["users", "blogs", "categories"]

    def setUp(self) -> None:
        self.client = APIClient()
        # Get test user from bd and set it as authenticated user
        user = User.objects.get(email="user1@email.com")
        self.client.force_authenticate(user=user)

    def test_retrieve(self):
        response = self.client.get(reverse("category-detail", kwargs={"pk": 1}))
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_list(self):
        response = self.client.get(reverse("category-list"))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(1, len(response.data))

    def test_create(self):
        response = self.client.post(
            reverse("category-list"), {"title": "Category 2", "slug": "category-2"}
        )
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual("Category 2", response.data["title"])

    def test_update(self):
        response = self.client.put(
            reverse("category-detail", kwargs={"pk": 1}),
            {"title": "Category 2", "slug": "category-2"},
        )
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual("Category 2", response.data["title"])

    def test_delete(self):
        response = self.client.delete(reverse("category-detail", kwargs={"pk": 1}))
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_delete_not_found(self):
        response = self.client.delete(reverse("category-detail", kwargs={"pk": 100}))
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
