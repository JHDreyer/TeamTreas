from django.db import models

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    location = models.CharField(max_length=255, default='None')
    image_url = models.CharField(max_length=2083, default='None')

