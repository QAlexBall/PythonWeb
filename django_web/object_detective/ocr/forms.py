from django import forms 
from django.forms import ModelForm
from django.contrib.auth.models import User
from ocr.models import Image, Record

class ImageForm(ModelForm):

    class Meta:
        model = Image
        fields = [
            'img_path',
        ]
