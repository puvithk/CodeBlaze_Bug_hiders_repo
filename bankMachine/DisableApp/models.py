from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
from django.contrib.auth.models import User
class Accountdetails(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    phone = models.BigIntegerField()
    acc = models.BigIntegerField()