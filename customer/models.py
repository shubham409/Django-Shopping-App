from django.db import models

# Create your models here.
class Customer(models.Model):

    

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return self.name

