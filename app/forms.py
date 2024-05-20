from django import forms
from . models import *

class addBlog(forms.ModelForm):
    class Meta:
        model = blogPost
        fields = [
            'title',
            'content',
            'pubDate',
            'author',
        ]

