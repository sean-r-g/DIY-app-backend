from django.db import models

# Create your models here.
class Guide(models.Model):
    title: models.CharField(max_length=100)
    subject: models.CharField(max_length=50)
    category: models.CharField(max_length=50)
    author: models.CharField(max_length=80)
    length: models.IntegerField()
    link: models.CharField(max_length=300)
    