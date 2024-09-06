from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from apps.blog.models import Blog, Category
from apps.blog.serializers import BlogSerializer, CategorySerializer
from apps.common.permissions import ReadOnly

from rest_framework import generics

from rest_framework import status
from .models import Comment
from .serializers import CommentCreateSerializer



class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BlogListView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (ReadOnly,)

    def get(self, request: Request) -> Response:
        blogs = Blog.objects.all()
        return Response(self.get_serializer(blogs, many=True).data)



class BlogItemView(generics.RetrieveAPIView):  # Change to RetrieveAPIView
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self, request, *args, **kwargs):
        blog = self.get_object()
        serializer = self.get_serializer(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateBlogPostView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request: Request) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateCommentView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
