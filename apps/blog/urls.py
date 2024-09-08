from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.blog.views import (
    BlogDetailView,
    BlogItemView,
    BlogListView,
    BlogPostView,
    CategoryViewSet,
    CommentCreateAPIView,
)

router = DefaultRouter(trailing_slash=False)
router.register(
    r"blog/categories",
    CategoryViewSet,
    basename="category",
)

urlpatterns = [
    path("blog", BlogListView.as_view(), name="blog_list"),
    path("blog/<int:pk>", BlogItemView.as_view(), name="blog_item"),
    path("blog/post", BlogPostView.as_view(), name="blog_post"),
    path("blog/comment", CommentCreateAPIView.as_view(), name="comment_create"),
    path("blog/blog/<int:pk>", BlogDetailView.as_view(), name="blog_details"),
    *router.urls,
]
