from rest_framework import serializers

from apps.blog.models import Category, Blog, Comment


# Create your serializers here.


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Blog
        fields = ['id', 'title', 'slug', 'body', 'posted', 'enabled', 'category', 'comments']

    def get_comments(self, obj):
        return [o for o in obj.comments.all().values_list('id', 'text').distinct()]


class BlogCreateSerializer(serializers.ModelSerializer):
    posted = serializers.ReadOnlyField()

    class Meta:
        model = Blog
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    blog_id = serializers.IntegerField()

    class Meta:
        model = Comment
        fields = ['blog_id', 'text']
