from django import forms
from .models import *


class BlogAdminForm(forms.ModelForm):
    Blog_content = forms.CharField(
        widget=forms.Textarea(attrs={'id': "richtext_field"}))

    class Meta:
        model = blog
        fields = "__all__"
