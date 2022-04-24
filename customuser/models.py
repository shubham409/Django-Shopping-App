from django import forms
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone




from django.contrib.auth.base_user import BaseUserManager
class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        # user.set_password(password)
        from django.contrib.auth.hashers import make_password
        user.password = make_password(password)
        user.save()
        return user



    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)




# username email first_name last_name is_staff is_active is_active date_joined
# we are taking username same as email 
class CustomUser(AbstractUser):
    from django.contrib.auth.password_validation import validate_password,password_validators_help_texts
    print(password_validators_help_texts)
    username = models.CharField(
    _("username"),
    max_length=150,
    help_text=_(
        "Mostly same as that of email, you may leave blank as it is not required"
    ),
    error_messages={
        "error ": _("Please enter valid username."),
    },
    blank=True,
    null=True
    ) 
    
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(_("password"),help_text="", max_length=128 , validators=[validate_password])
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = None

    objects = CustomUserManager()
    

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

