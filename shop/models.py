from django.db import models
from timestamp.models import Timestamp
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Shop(Timestamp):
    user = models.ForeignKey("customuser.CustomUser", on_delete=models.CASCADE)
    title = models.CharField(_("title of the shop") ,max_length=400 ,blank=True, null=True)
    shop_name = models.CharField(_("Owner of Shop") ,max_length=400 ,blank=True, null=True)
    owner = models.CharField(_("Owner of Shop") ,max_length=400 ,blank=True, null=True)
    address = models.CharField(_("Location of the Shop") ,max_length=400 ,blank=True, null=True)
    # need validation 
    pincode = models.CharField(_("pincode") ,max_length=20 ,blank=True, null=True)
    # need validation 
    city = models.CharField(_("title of the shop") ,max_length=100 ,blank=True, null=True)
    # need validation
    state = models.CharField(_("title of the shop") ,max_length=100 ,blank=True, null=True)
    
    product_count = models.CharField(_("title of the shop") ,max_length=50 ,blank=True, null=True)
    
    # need validations 
    mobile_no = models.CharField(_("title of the shop") ,max_length=400 ,blank=True, null=True)
    alter_phone_no = models.CharField(_("title of the shop") ,max_length=400 ,blank=True, null=True)
    
    # need validator 
    mail = models.CharField(_("title of the shop") ,max_length=400 ,blank=True, null=True)















