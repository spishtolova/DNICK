from operator import truediv
from django.contrib.auth.models import User

from django.db import models

class Candy(models.Model):
   name = models.CharField(max_length=64, null=True, blank=True)
   price = models.IntegerField(null=True, blank=True)
   quantity = models.IntegerField(null=True, blank=True)
   image = models.ImageField(null=True, blank=True, upload_to='candies/')
   supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE, null=True, blank=True, related_name='candies')

   def __str__(self):
       return (f"{self.name} {self.price}")


class Supplier(models.Model):
    firstName = models.CharField(max_length=64, null=True, blank=True)
    lastName = models.CharField(max_length=64, null=True, blank=True)
    company = models.CharField(max_length=64, null=True, blank=True)
    user = models.ForeignKey(User, null = True, blank = True, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.firstName} {self.lastName} {self.company}")




