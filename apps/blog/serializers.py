from rest_framework import serializers

from apps.blog.models import Blog, Category, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class CommentCreateSerializer(serializers.ModelSerializer):
    blog_id = serializers.IntegerField()

    class Meta:
        model = Comment
        fields = ["blog_id", "text"]

    def create(self, validated_data):
        blog_id = validated_data.get("blog_id")
        text = validated_data.get("text")

        try:
            blog = Blog.objects.get(id=blog_id)
        except Blog.DoesNotExist as e:
            raise serializers.ValidationError("Blog post does not exist.") from e

        comment = Comment.objects.create(blog=blog, text=text)
        return comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "blog_id", "text"]
