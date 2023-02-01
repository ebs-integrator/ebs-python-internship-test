from django.db import models
from apps.blog.models import Category, Blog


class Comment(models.Model):
    text = models.CharField(max_length=255, unique=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
