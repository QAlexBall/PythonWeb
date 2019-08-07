from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Image(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img_path = models.ImageField(upload_to='ocr/image/', blank=True, null=True, max_length=500)
    upload_date = models.DateTimeField(auto_now=True)
    tag = models.TextField()

class Favorite(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    add_date = models.DateTimeField(auto_now=True)

class Record(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_image = models.ForeignKey(Image, on_delete=models.CASCADE)
    record_date = models.DateTimeField(auto_now=True)
    result = models.TextField()
