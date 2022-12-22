from blog.models import Post

from django import template
register = template.Library() 

@register.inclusion_tag('recent_posts.html')
def render_recent_blogposts():
    return {
        
        'post_list': Post.objects.all()
    }