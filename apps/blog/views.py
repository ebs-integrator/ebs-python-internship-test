from rest_framework import status, viewsets
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from apps.blog.models import Blog, Category, Comment
from apps.blog.serializers import BlogSerializer, CategorySerializer, CommentSerializer
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


class BlogCreateView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        blog = serializer.save()
        return Response(self.get_serializer(blog).data, status=status.HTTP_201_CREATED)

class CommentCreateView(GenericAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        comment = serializer.save()
        return Response(self.get_serializer(comment).data, status=status.HTTP_201_CREATED)

class BlogItemCommentListView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (ReadOnly, IsAuthenticated)

    def get(self, request: Request, pk: int) -> Response:
        blog: Blog = get_object_or_404(Blog.objects.all(), pk=pk)
        comment_ = Comment.objects.filter(blog=pk)
        return Response({
            "blog": self.get_serializer(blog).data,
            "comment": CommentSerializer(comment_, many=True).data,
        })
