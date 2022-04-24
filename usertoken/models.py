from sqlite3 import Timestamp
from django.db import models
from rest_framework.authtoken.models import Token
from timestamp.models import Timestamp
from django.utils.translation import gettext_lazy as _
from customuser.models import CustomUser
# Create your models here.



# This is the token generated when user sign in and vill be valid till
# one day it will be given by when when user will verify thenselves with otp
class Token(Timestamp):
    token = models.ForeignKey(Token, verbose_name=_(""), on_delete=models.CASCADE)
    user = models.OneToOneField(CustomUser)




