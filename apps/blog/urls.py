from django.urls import path

from apps.blog.views import CategoryViewSet, BlogListView, BlogItemView, CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(
    r"categories",
    CategoryViewSet,
    basename="category",
)
router.register(
    r"comments",
    CommentViewSet,
    basename="comment",
)

urlpatterns = router.urls

urlpatterns += [
    path("blog", BlogListView.as_view(), name="blog_list"),
    path("blog/<int:pk>", BlogItemView.as_view(), name="blog_item"),
]
