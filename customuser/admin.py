from django.contrib import admin
from .models import CustomUser
from django import forms
# Register your models here.
from django.contrib.auth.password_validation import validate_password,password_validators_help_texts

class CustomUserAdmin(admin.ModelAdmin):
    st = 'username email password first_name last_name is_staff is_active is_superuser last_login groups user_permissions'.split(' ')
    print(tuple(st))
    print(validate_password)
    #  this field is used to set in which order we see the fields in the admin
    #  form, not it is different from list display which only chnages in 
    #  table of admin showing objects
    fields = st
    pass 

    
admin.site.register(CustomUser,CustomUserAdmin)