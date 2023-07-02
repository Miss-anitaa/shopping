from django.db import models
from django.contrib.auth.models import AbstractUser 

class CustomUser(AbstractUser):
    city = models.ForeignKey('shop.City', null=True, blank=False ,on_delete=models.CASCADE)
    pass