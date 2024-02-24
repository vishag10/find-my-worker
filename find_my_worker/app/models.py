from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
# Create your models here.
class CustomUser(AbstractUser):
    register_status=(
        ('approve','approve'),
        ('pending','pending'),
        ('reject','reject'),
    )
    phone_number=models.CharField(max_length=10)
    user_type=models.CharField(choices=register_status,default='pending',max_length=50)


