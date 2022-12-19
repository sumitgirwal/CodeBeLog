from django.contrib import admin
from .models import Post


# Register your models here.

class PostAdminModel(admin.ModelAdmin):
    list_display = ['id', 'title', 'updated_at']
    ordering = ['id', 'title', 'updated_at']


admin.site.register(Post, PostAdminModel)