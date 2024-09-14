from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.blog.views import BlogCreatePost, BlogItemView, BlogListView, CategoryViewSet, CommentsCreateView

router = DefaultRouter(trailing_slash=False)
router.register(
    r"blog/categories",
    CategoryViewSet,
    basename="category",
)

urlpatterns = [
    path("blog", BlogListView.as_view(), name="blog_list"),
    path("blog/<int:pk>", BlogItemView.as_view(), name="blog_item"),
    path("blog/create-post", BlogCreatePost.as_view(), name="create_post"),
    path("blog/create-comment", CommentsCreateView.as_view(), name="create_comment"),
    *router.urls,
]
