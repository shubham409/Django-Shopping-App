from itertools import product
from django.db import models

from shopkeeper.models import Shopkeeper

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 100,blank=True,null=False)
    user = models.OneToOneField(Shopkeeper, on_delete=models.CASCADE)