from django import forms
from .models import Post, Category, Comment

class CustomMMCF(forms.ModelMultipleChoiceField):       
    def label_from_instance(self, category):
        return category.name

class PostForm(forms.ModelForm):
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