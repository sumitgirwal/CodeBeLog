from django.forms import ModelForm
from .models import Post

# Creating model form
class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'description']
        