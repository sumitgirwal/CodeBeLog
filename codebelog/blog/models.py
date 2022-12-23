from django.db import models
from account.models import User


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
    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    view = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=255, unique=True)
    status = models.IntegerField(choices=STATUS, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return str(self.id)+' | '+self.title
    
    