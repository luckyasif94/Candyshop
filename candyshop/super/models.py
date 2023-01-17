from django.db import models
from django.db.models import Model

# Create your models here.

class Login(Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

