from django.contrib import admin
from blog.models import Category, Tag, Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)


