from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.blog.models import Category, Blog , Comments
from apps.blog.serializers import CategorySerializer, BlogSerializer , CommentSerializer
from apps.common.permissions import ReadOnly


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comments.objects.all()

class BlogListView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = ()

    def get(self, request):
        blogs = Blog.objects.all()
        return Response(BlogSerializer(blogs, many=True).data)
    
    def post(self, request):
        data = request.data
        new_blog = Blog(
            title=data.get('title'),
            slug=data.get('slug'),
            body=data.get('body'),
            enabled=data.get('enabled'),
            category= Category.objects.get(pk=data.get('category'))     
            )
        new_blog.save()
        return Response(status=200)


class BlogItemView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (ReadOnly,)

    def get(self, request, pk):
        blog = get_object_or_404(Blog.objects.filter(pk=pk))
        comments = Comments.objects.filter(blog_id=pk)

        return Response([BlogSerializer(blog).data,CommentSerializer(comments , many=True).data])
