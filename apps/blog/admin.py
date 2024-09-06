from django.contrib import admin

from apps.blog.models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'enabled')  # Display blog title and enabled status in the list view

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
