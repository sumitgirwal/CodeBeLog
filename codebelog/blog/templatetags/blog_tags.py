from blog.models import Post, Category
from django import template

register = template.Library()

@register.inclusion_tag('recent_posts.html')
def render_recent_blogposts():
    return {
        'post_list': Post.objects.all()
    }

@register.inclusion_tag('index.html')
def render_category():
    return {
        'category_list': Category.objects.all()
    }


@register.simple_tag
def breadcrumb_schema():
    return "http://schema.org/BreadcrumbList"


@register.simple_tag
def get_categories():
     
    return {
        'cats':Category.objects.all()
    }
