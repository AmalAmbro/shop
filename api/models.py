from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Shop(models.Model):
    name = models.CharField(max_length=64)
    price = models.CharField(max_length=32)
    image = models.FileField(upload_to='fruits/')
    
    def __str__(self):
        return self.name
