from django.contrib import admin
from blog.models import Post, Category, Comment


# Post admin model
class PostAdminModel(admin.ModelAdmin):
    list_display = ['id', 'title', 'auther', 'status', 'created_at']
    list_display_links = ['id', 'title', ]
    list_filter = ("status",)
    search_fields = ['title', 'subtitle', 'slug']
    ordering = ['id', 'auther' , 'title', 'created_at']
    # auto fill for slug
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdminModel)
admin.site.register(Category)
admin.site.register(Comment)