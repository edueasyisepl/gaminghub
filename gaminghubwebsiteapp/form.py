from django import forms
from .models import image_mod

class Image_model(forms.Form):
    class Meta:
        model = image_mod
        fields = ("image")