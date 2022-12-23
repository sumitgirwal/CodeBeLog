from django import template
 
register = template.Library()
 
 
@register.simple_tag
def breadcrumb_schema():
    return "http://schema.org/BreadcrumbList"
 
 
@register.inclusion_tag('core/breadcrumb_home.html')
def breadcrumb_home(url='/', title=''):
    return {
        'url': url,
        'title': title
    }
 
 
@register.inclusion_tag('core/breadcrumb_item.html')
def breadcrumb_item(url, title, position):
    return {
        'url': url,
        'title': title,
        'position': position
    }
 
 
@register.inclusion_tag('core/breadcrumb_active.html')
def breadcrumb_active(url, title, position):
    return {
        'url': url,
        'title': title,
        'position': position
    }