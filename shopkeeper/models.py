from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Shopkeeper(models.Model):
    # one to one field 
    user = models.OneToOneField('customuser.CustomUser' , on_delete=models.CASCADE)
    # one to many field 
    shop = models.ForeignKey("shop.Shop", help_text=_("shop of the shopkeeper"), on_delete=models.CASCADE)
    
    total_shops = models.CharField(max_length=30 , blank=True, null=True)

    class Meta:
        verbose_name = _("Shopkeeper")
        verbose_name_plural = _("Shopkeepers")

