from rest_framework import serializers

from apps.blog.models import Category, Blog
from apps.comments.models import Comment
from apps.comments.serializers import CommSerializer




# Create your serializers here.


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

class TotalSerializer(serializers.ModelSerializer):
     comment = CommSerializer(many = True,read_only=True)
     blog = BlogSerializer(read_only=True)
     class Meta:
        model = Blog
        fields = ("id","blog","comment")
        