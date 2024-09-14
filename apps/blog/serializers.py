from rest_framework import serializers

from apps.blog.models import Blog, Category, Comments


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CommentsSerializer(serializers.ModelSerializer):
    blog_id = serializers.IntegerField()

    class Meta:
        model = Comments
        fields = ["blog_id", "text"]

    def validate_blog_id(self, value):
        if not Blog.objects.filter(id=value).exists():
            raise serializers.ValidationError("Blog with this ID does not exist.")
        return value

    def create(self, validate_data):
        blog_id = validate_data.pop("blog_id")
        blog = Blog.objects.get(id=blog_id)
        comment = Comments.objects.create(blog=blog, **validate_data)

        return comment


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
