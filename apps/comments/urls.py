from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.comments.views import CommItemPost

urlpatterns = [
    path("input",  CommItemPost.as_view(), name="comment_input"),
]
