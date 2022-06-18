from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Guide(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    author = models.CharField(null=True, max_length=80)
    length = models.IntegerField()
    link = models.CharField(max_length=300)
