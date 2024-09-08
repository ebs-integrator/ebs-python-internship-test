from rest_framework import serializers

from apps.blog.models import Blog, Category, Comments


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"


class BlogDetailsSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    def get_comments(self, pk):
        comments = Comments.objects.filter(blog=pk)
        return CommentsSerializer(comments, many=True).data

    class Meta:
        model = Blog
        fields = ["id", "title", "slug", "body", "posted", "category", "enabled", "comments"]
