from django.db import models

class Orders(models.Model):
    username = models.CharField(max_length = 100)
    productname = models.CharField(max_length = 100)
    cost = models.IntegerField()
    customer_address = models.CharField(max_length = 250)
    city = models.CharField(max_length = 50)
    pincode = models.IntegerField()
    phone = models.BigIntegerField()


    def __str__(self):
        return self.productname

    def getcost(self):
        return '₹' + str(self.cost)

    def getaddress(self):
        return "Delievering to " + self.customer_address
