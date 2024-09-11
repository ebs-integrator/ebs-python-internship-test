from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True)


class Blog(models.Model):
    enabled = models.BooleanField(default=True)
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comments(models.Model):
    text = models.CharField(max_length=255, db_index=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
