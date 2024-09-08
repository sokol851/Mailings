from django import forms
from mailings.forms import StyleFormMixin
from .models import Blog


class BlogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'image', 'is_published']
