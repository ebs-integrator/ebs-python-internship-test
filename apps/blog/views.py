from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.blog.models import Category, Blog
from apps.blog.serializers import CategorySerializer, BlogSerializer
from apps.common.permissions import ReadOnly, All
from drf_util.decorators import serialize_decorator


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = (All,)
    queryset = Category.objects.all()


class BlogListView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (ReadOnly,)

    def get(self, request):
        blogs = Blog.objects.all()
        return Response(BlogSerializer(blogs, many=True).data)


class BlogItemView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (All,)

    def get(self, request, pk):
        blog = get_object_or_404(Blog.objects.filter(pk=pk))
        return Response(BlogSerializer(blog).data)


    @serialize_decorator(BlogSerializer)
    def post(self, request, pk):
        validated_data = request.serializer.validated_data

        title = validated_data.pop("title")
        slug = validated_data.pop("slug")
        body = validated_data.pop("body")
        category = validated_data.pop("category")
        enabled = validated_data.pop("enabled")

        blog = Blog.objects.create(
            category=category, title=title, slug=slug, body=body, enabled=enabled
        )

        blog.save()

        return Response(BlogSerializer(blog).data)
