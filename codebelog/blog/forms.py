from django import forms
from .models import Post, Category, Comment

from tinymce.widgets import TinyMCE

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class CustomMMCF(forms.ModelMultipleChoiceField):       
    def label_from_instance(self, category):
        return category.name

class PostForm(forms.ModelForm):
    
    # Content field
    description = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    category = CustomMMCF(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Post 
        fields = [
            'title',
            'subtitle',
            'description',
            'category'
        ]
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
         # Sort categories to alphabetically order
        self.fields['category'].queryset = Category.objects.all().order_by('name')



class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = [
            'title',
            'subtitle',
            'description',
            'slug',
            'category'
        ]
    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']



# class PostForm(forms.ModelForm):
#     category = CustomMMCF(
#         queryset=Category.objects.all(),
#         widget=forms.CheckboxSelectMultiple
#     )

#     class Meta:
#         model = Post 
#         fields = [
#             'title',
#             'subtitle',
#             'description',
#             'slug',
#             'category'
#         ]
    
#     def __init__(self, *args, **kwargs):
#         super(PostForm, self).__init__(*args, **kwargs)
#          # Sort categories to alphabetically order
#         self.fields['category'].queryset = Category.objects.order_by('name')