from django.contrib import admin

from apps.blog.models import Blog, Category, Comments

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Comments)
