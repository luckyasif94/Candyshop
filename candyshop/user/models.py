from django.db import models
from django.db.models import Model

# Create your models here.

class Product(Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    details = models.TextField()
    stock = models.IntegerField()
    image1 = models.FileField(upload_to='img')
    image2 = models.FileField(upload_to='img')

class Review(Model):
    review = models.TextField()
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Orders(Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    addressline1 = models.TextField()
    addressline2 = models.TextField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=50,default="Not Approved")