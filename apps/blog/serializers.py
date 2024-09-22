from rest_framework import serializers

from apps.blog.models import Blog, BlogComments, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComments
        fields = ("Comments", "blog")


class BlogSerializer(serializers.ModelSerializer):
    comments = serializers.SlugRelatedField(many=True, read_only=True, slug_field="Comments")

    class Meta:
        model = Blog
        fields = "__all__"  # ("title", "slug", "body", "enabled", "category")
