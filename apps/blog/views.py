from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from apps.blog.models import Blog, Category, Comments
from apps.blog.serializers import BlogSerializer, CategorySerializer, CommentSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BlogListView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (AllowAny,)

    def get(self, request: Request) -> Response:
        blogs = Blog.objects.all()
        return Response(self.get_serializer(blogs, many=True).data)


class BlogItemView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (AllowAny,)

    def get(self, request: Request, pk: int) -> Response:
        blog: Blog = get_object_or_404(Blog.objects.all(), pk=pk)
        return Response(self.get_serializer(blog).data)


class AddBlockPost(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (AllowAny,)

    def post(self, request: Request) -> Response:
        #  Validate data
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        blog = Blog.objects.create(**validated_data)
        blog.save()

        return Response(self.serializer_class(blog).data)


class AddBlockComment(GenericAPIView):
    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        comment = Comments.objects.create(**validated_data)
        comment.save()

        return Response(self.serializer_class(comment).data)
