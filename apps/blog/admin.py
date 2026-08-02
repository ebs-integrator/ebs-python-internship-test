from django.contrib import admin

from apps.blog.models import Blog, Category


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "enabled")


admin.site.register(Category)
