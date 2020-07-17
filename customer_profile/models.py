from django.db import models

# Create your models here.
class ServiceProvider(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    location = models.CharField(max_length=255, default='None')
    services = models.CharField(max_length= 3000)
    products = models.CharField(max_length= 3000, default='None')

    logo = models.ImageField(default='None')


class Commerce(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    location = models.CharField(max_length=255, default='None')
    services = models.CharField(max_length= 3000)
    products = models.CharField(max_length= 3000, default='None')

    logo = models.ImageField(default='None')
