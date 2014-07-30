__author__ = 'kevin'
from django import forms
from django.forms import ModelForm
from main.models import Post

class PostForm(ModelForm):
    author_id = forms.CharField(widget=forms.HiddenInput(), required=False)
    recipient_id = forms.CharField(widget=forms.HiddenInput(), required=False)
    author_name = forms.CharField(widget=forms.HiddenInput(), required=False)
    recipient_name = forms.CharField(widget=forms.HiddenInput(), required=False)
    good = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'good', 'class':"form-control"}))
    bad = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'bad', 'class':"form-control"}))

    class Meta:
        model = Post
        fields = ['author_id', 'recipient_id', 'author_name', 'recipient_name', 'good', 'bad']