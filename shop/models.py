from django.db import models

# Create your models here.

class Articles(models.Model):
    name = models.CharField(max_length=200, default="Article")
    stock = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    image_url = models.CharField(max_length=200, default="url")
