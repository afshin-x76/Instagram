from django import forms
from .models import Post, Comment

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class CreateCommentForm(forms.ModelForm):
    class Meta:
        models = Comment
        fields = '__all__'