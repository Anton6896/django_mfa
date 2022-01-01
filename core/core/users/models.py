from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    password = models.CharField(_('password'), max_length=128)
