from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=225)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=2500) 


class Offer(models.Model):
    code = models.CharField(max_length=16)
    description = models.CharField(max_length=2550)
    discount = models.FloatField()