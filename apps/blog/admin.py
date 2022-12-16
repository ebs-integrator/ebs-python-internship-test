from django.contrib import admin

from apps.blog.models import Blog, Category

admin.site.register(Blog)
admin.site.register(Category)
