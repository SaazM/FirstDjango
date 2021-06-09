from django import forms
from .models import Post

class PostForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "placeholder":"Leave a comment here",
        "id":"floatingTextarea2",
    }))
    description = forms.CharField(widget=forms.TextInput(attrs={
        "class":"form-control",
        "placeholder":"Leave a comment here",
        "id":"floatingTextarea2",
        "style":"height: 100px"
    }))
    image = forms.FileField(widget=forms.FileInput(attrs={
        "class":"form-control", 
        "type":"file",
        "id":"formFile"
    }))

