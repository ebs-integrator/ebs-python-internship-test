from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.blog.views import BlogItemView, BlogListView, CategoryViewSet

router = DefaultRouter(trailing_slash=False)
router.register(
    r"blog/categories",
    CategoryViewSet,
    basename="category",
)

urlpatterns = [
    path("blog", BlogListView.as_view(), name="blog_list"),
    path("blog/<int:pk>", BlogItemView.as_view(), name="blog_item"),
    *router.urls,
]
