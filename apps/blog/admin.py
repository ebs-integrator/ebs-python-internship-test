from django.contrib import admin

from apps.blog.models import Blog, Category, Comments

admin.site.register(Blog)
admin.site.register(Category)


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ("text", "blog", "id")
    search_fields = ("text",)
    list_filter = ("blog",)
