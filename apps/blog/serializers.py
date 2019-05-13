from django.contrib.auth.models import User
from rest_framework import serializers

from apps.blog.models import Category, Blog


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
