from django.db import models

class Customer(models.Model):
    FirstName = models.CharField(max_length = 30)
    LastName = models.CharField(max_length = 30)
    Email = models.EmailField(max_length = 100)
    Phone = models.BigIntegerField()
    Address = models.TextField()

    def __str__(self):
        return self.FirstName + " " + self.LastName
