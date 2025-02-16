from django import forms
from .models import ShortenedURL

#this django form allos the user to input a url to be shortened
class URLForm(forms.ModelForm):
    class Meta:
        model = ShortenedURL
        fields = ['original_url']
