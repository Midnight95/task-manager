from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _


class User(AbstractUser):
    username = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_('Username')
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name=_('First name')
        )
    last_name = models.CharField(
        max_length=100,
        verbose_name=_('Last name')
    )

    def __str__(self):
        return self.username
