from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
