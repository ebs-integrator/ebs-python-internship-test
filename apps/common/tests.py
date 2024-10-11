import json

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.test import RequestFactory, TestCase
from django.urls import path
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from apps.common.middlewares import ApiMiddleware


class TestCommon(TestCase):
    fixtures = ["users"]

    def setUp(self) -> None:
        self.client = APIClient()
        # check data in fixture json file
        self.test_user1 = User.objects.get(email="user1@email.com")

    def test_health_view(self) -> None:
        response = self.client.get(reverse("health_view"))
        self.assertEqual(response.status_code, 200)

    def test_protected_view(self) -> None:
        self.client.force_authenticate(user=self.test_user1)
        response = self.client.get(reverse("protected_view"))
        self.assertEqual(response.status_code, 200)


# Mock view that raises an exception
def view_that_raises(request):  # noqa: E302
    raise ValueError("Test exception")


urlpatterns = [
    path("exception/", view_that_raises),
]


class ApiMiddlewareExceptionTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.middleware = ApiMiddleware

    def test_process_exception_returns_json_response(self):
        request = self.factory.get("/exception/")
        response = None

        # Simulate request processing and exception handling
        try:
            self.middleware.process_request(request)
            view_that_raises(request)
        except ValueError as e:
            response = self.middleware.process_exception(request, e)

        # Ensure a response was returned
        self.assertIsNotNone(response)
        self.assertIsInstance(response, JsonResponse)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response["Content-Type"], "application/json")

        # Validate response content
        content = json.loads(response.content)
        self.assertIn("exception", content)
        self.assertIn("detail", content)
        self.assertEqual(content["exception"], "Test exception")
        self.assertEqual(content["detail"], "Something Went Wrong. Please contact support")
