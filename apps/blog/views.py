from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from apps.blog.models import Category, Blog
from apps.blog.serializers import CategorySerializer, BlogSerializer, TotalSerializer
from apps.common.permissions import ReadOnly
from drf_util.decorators import serialize_decorator
from apps.comments.models import Comment
from apps.comments.serializers import CommSerializer


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
    

class BlogItemView(GenericAPIView):
    serializer_class = TotalSerializer
    permission_classes = (ReadOnly,)

    def get(self, request, pk):
        blog = get_object_or_404(TotalSerializer.objects.filter(pk=pk))
        return Response(TotalSerializer(blog).data)

class BlogItemPost(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (AllowAny,)

    @serialize_decorator(BlogSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        blog = Blog.objects.create(
            **validated_data,
        )
        blog.save()

        return Response(BlogSerializer(blog).data)