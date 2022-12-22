from django.contrib import admin
from .models import Post, Category


# Register your models here.

class PostAdminModel(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'slug', 'status', 'updated_at']
    list_filter = ("status",)
    search_fields = ['title']
    ordering = ['id', 'user' , 'title', 'updated_at']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdminModel)
admin.site.register(Category)