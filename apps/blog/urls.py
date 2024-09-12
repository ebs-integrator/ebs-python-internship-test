from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.blog.views import BlogAddView, BlogItemDetailView, BlogItemView, BlogListView, CategoryViewSet, CommentAddView

router = DefaultRouter(trailing_slash=False)
router.register(
    r"blog/categories",
    CategoryViewSet,
    basename="category",
)

urlpatterns = [
    path("blog", BlogListView.as_view(), name="blog_list"),
    path("blog/<int:pk>", BlogItemView.as_view(), name="blog_item"),
    path("blog/blog/<int:pk>", BlogItemDetailView.as_view(), name="blog_detail_comments"),
    path("blog/add", BlogAddView.as_view(), name="blog_add"),
    path("blog/comment", CommentAddView.as_view(), name="blog_add_comment"),
    *router.urls,
]
