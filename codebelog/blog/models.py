from django.db import models

from account.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    view = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return str(self.id)+' '+self.title
    
    