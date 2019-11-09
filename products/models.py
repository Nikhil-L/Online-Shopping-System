from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField()
    description = models.TextField(blank = True)
    cost = models.IntegerField(default = 50, blank = True)
    details = models.TextField()
    seller = models.CharField(max_length = 100, default = 'abc', blank = True)

    def __str__(self):
        return self.name

    def display_cost(self):
        return '₹' + str(self.cost)

    def snippet(self):
        return self.details[0:50] + "..."
