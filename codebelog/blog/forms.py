from django.forms import ModelForm
from .models import Post

# Creating model form
class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'description']
    
    def __init__(self, *args, **kwargs):
        # Allows you to pass the user in from the request, or just set the property
        if not hasattr(self, 'user'):
            self.user = kwargs.pop('user')
        super(PostForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super(PostForm, self).save(commit=False)
        user.user = self.user
        if commit:
            user.save()
        return user
        