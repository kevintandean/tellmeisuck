__author__ = 'kevin'
from django import forms
from django.forms import ModelForm
from main.models import Post

class PostForm(ModelForm):
    author = forms.CharField(widget=forms.HiddenInput(), required=False)
    recipient = forms.CharField(widget=forms.HiddenInput(), required=False)
    # author_name = forms.CharField(widget=forms.HiddenInput(), required=False)
    # recipient_name = forms.CharField(widget=forms.HiddenInput(), required=False)
    good = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'good', 'class':"form-control"}))
    bad = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'bad', 'class':"form-control"}))

    class Meta:
        model = Post
        fields = ['author', 'recipient','good', 'bad']