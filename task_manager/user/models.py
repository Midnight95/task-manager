from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=100)
    USERNAME_FIELD = 'email'
