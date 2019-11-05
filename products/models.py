from django.db import models

# Create your models here.

Class Product(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField()
    detail = models.TextField()
