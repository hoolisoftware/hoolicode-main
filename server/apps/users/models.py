from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ACCOUNT_TYPES = (
        ('customer', 'Customer'),
        ('employee', 'Employee')
    )

    avatar = models.ImageField('avatar', upload_to='users/avatar/', default='users/avatar/default/default.png')
    account_type = models.CharField('account type', max_length=50, choices=ACCOUNT_TYPES, default='customer')
    balance = models.IntegerField(default=0)
    xp = models.IntegerField(default=0)