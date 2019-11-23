from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    FirstName = models.CharField(max_length = 30)
    LastName = models.CharField(max_length = 30)
    UserName = models.ForeignKey(User,default = 'None', blank = True, on_delete = models.CASCADE)
    Email = models.EmailField(max_length = 100)
    Phone = models.BigIntegerField()
    Address = models.CharField(max_length = 250)
    City = models.CharField(max_length = 50)
    Pincode = models.IntegerField()

    def __str__(self):
        return self.FirstName + " " + self.LastName
