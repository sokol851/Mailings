from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'image', 'is_published', 'owner')
    list_filter = ('title', 'is_published',)
    search_fields = ('title',)
