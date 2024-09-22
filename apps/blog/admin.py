from django.contrib import admin

from apps.blog.models import Blog, BlogComments, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "enabled")
    list_display_links = ("title",)
    list_editable = ("enabled",)
    short_description = "Blog published status"


class BlogAdminComments(admin.ModelAdmin):
    list_display = ["Comments", "blog"]
    list_display_links = [
        "Comments",
    ]
    # list_editable = ('Comments',)
    short_description = "Blog comments"


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(BlogComments, BlogAdminComments)
