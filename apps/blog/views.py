from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from apps.blog.models import Blog, Category, Comment
from apps.blog.serializers import BlogDetailSerializer, BlogSerializer, CategorySerializer, CommentSerializer
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

    def get(self, pk: int) -> Response:
        blog: Blog = get_object_or_404(Blog.objects.all(), pk=pk)
        return Response(self.get_serializer(blog).data)


# In endpoint /blog/blog/{id} return the Blog post object and list of comments.
class BlogItemDetailView(GenericAPIView):
    serializer_class = BlogDetailSerializer
    permission_classes = (ReadOnly,)

    def get(self, request: Request, pk: int) -> Response:
        blog: Blog = get_object_or_404(Blog.objects.all(), pk=pk)
        return Response(self.get_serializer(blog).data)


# Make an endpoint for create a blog post that will add a new record in blog table
class BlogAddView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()

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


# Create an endpoint that creates a comment to a blog post (input: blog_id, text)
class CommentAddView(GenericAPIView):
    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def post(self, request: Request) -> Response:
        #  Validate data
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        # Create comment
        comment = Comment.objects.create(
            **validated_data,
        )
        comment.save()

        return Response(self.serializer_class(comment).data)
