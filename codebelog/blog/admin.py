from django.contrib import admin
from blog.models import Post, Category


# Post admin model
class PostAdminModel(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'status', 'created_at']
    list_display_links = ['id', 'title', ]
    list_filter = ("status",)
    search_fields = ['title', 'subtitle', 'slug']
    ordering = ['id', 'user' , 'title', 'created_at']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdminModel)
admin.site.register(Category)