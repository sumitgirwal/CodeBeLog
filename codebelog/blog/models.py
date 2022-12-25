from django.db import models
from account.models import User
from datetime import  timezone

# Blog post status
STATUS = (
    (0, "Public"),
    (1, "Private")
)

# Categories
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Blog Categories"

    def __str__(self):
        return str(self.id)+' | '+self.name


# Blog posts
class Post(models.Model):
    # blog details
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    # unique for every title
    slug = models.SlugField(max_length=255, unique=True)

    # foreign key
    auther = models.ForeignKey(User, on_delete=models.CASCADE)

    # multi select field
    category = models.ManyToManyField(Category)
    
    # default values
    status = models.IntegerField(choices=STATUS, default=0)
    view = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return str(self.id)+' | '+self.title
    
    