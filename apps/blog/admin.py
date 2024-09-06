from django.contrib import admin

from apps.blog.models import Blog, Category, Comment

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'enabled')  
class CategoryAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'text', 'created_at')  
    search_fields = ('blog__title', 'text')        
    list_filter = ('created_at',)                  

admin.site.register(Comment, CommentAdmin) 
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
