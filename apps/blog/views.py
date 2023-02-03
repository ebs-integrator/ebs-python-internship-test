from rest_framework import viewsets, status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from apps.blog.models import Category, Blog, Comment
from apps.blog.serializers import CategorySerializer, BlogSerializer, BlogCreateSerializer, CommentSerializer
from apps.common.permissions import ReadOnly


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BlogListView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (ReadOnly,)

    def get(self, request):
        blogs = Blog.objects.all()
        return Response(BlogSerializer(blogs, many=True).data)


class BlogCreateView(GenericAPIView):
    serializer_class = BlogCreateSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def post(self, request):
        serializer = BlogCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class BlogCommentCreateView(GenericAPIView):
    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def post(self, request):
        blog_id = request.data['blog_id']
        try:
            blog = Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist:
            return Response({'error': f'Blog with id {blog_id} does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
        comment = Comment.objects.create(blog=blog, text=request.data['text'])
        comment.save()
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class BlogItemView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (ReadOnly, IsAuthenticated)

    def get(self, request, pk):
        blog = get_object_or_404(Blog.objects.filter(pk=pk))
        return Response(BlogSerializer(blog).data)
