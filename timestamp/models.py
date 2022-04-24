from datetime import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Timestamp(models.Model):
    created_on = models.DateTimeField(_("datetime at which this object has been first created ") , blank=True, null=True, default=datetime.now())
    modified_on = models.DateTimeField(_("datetime at which this object was modifed last time") ,blank=True, null=True, default=datetime.now())


