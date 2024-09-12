from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, db_index=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # Add in Blog model a boolean field enabled to make some posts published or unpublished
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# Create a new model Comments with text and blog foreign key
class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    text = models.CharField(max_length=255, unique=False)

    class Meta:
        unique_together = ["text"]
        ordering = ["text"]

    def __str__(self):
        return self.text
