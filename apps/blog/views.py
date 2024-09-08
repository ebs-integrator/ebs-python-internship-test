from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.blog.models import Blog, Category
from apps.blog.serializers import BlogDetailsSerializer, BlogSerializer, CategorySerializer, CommentsSerializer
from apps.common.permissions import ReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BlogListView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (ReadOnly,)

    def get(self, request: Request) -> Response:
        blogs = Blog.objects.all()
        return Response(self.get_serializer(blogs, many=True).data)


class BlogItemView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (ReadOnly, IsAuthenticated)

    def get(self, request: Request, pk: int) -> Response:
        blog: Blog = get_object_or_404(Blog.objects.all(), pk=pk)
        return Response(self.get_serializer(blog).data)


class BlogPostView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request: Request) -> Response:
        #  Validate data
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        # Create blog
        blog = Blog.objects.create(
            **validated_data,
        )
        blog.save()
        return Response(self.serializer_class(blog).data)


class CommentCreateAPIView(CreateAPIView):
    serializer_class = CommentsSerializer
    permission_classes = (IsAuthenticated,)


class BlogDetailView(APIView):
    def get(self, request: Request, pk: int) -> Response:
        blog: Blog = get_object_or_404(Blog.objects.all(), pk=pk)
        serializer = BlogDetailsSerializer(blog)
        return Response(serializer.data)
