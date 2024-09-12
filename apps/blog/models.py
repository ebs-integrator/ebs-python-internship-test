from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True)

    def __str__(self) -> str:
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    enabled = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title + "   Status=" + str("Enabled" if self.enabled else "Disabled")

class Comment(models.Model):
    body = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return "Comments for Admin [blog.title]="+self.blog.title+ "     [comment.body]=" +self.body