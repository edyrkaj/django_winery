from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from passlib.hash import pbkdf2_sha256

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):  # __unicode__ on Python 2
      return self.name

class Company(models.Model):
    name = models.CharField(max_length=100)
    award = models.ImageField(upload_to='C:/Users/Admin/Desktop/winerymobile/img/award',null=True)
    about = models.TextField()
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='C:/Users/Admin/Desktop/winerymobile/img/company')

    def __str__(self):
      return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    company = models.ForeignKey(Company)
    quantity = models.DecimalField(max_digits=8, decimal_places=2,default=0.0)
    image = models.FileField(upload_to='C:/Users/Admin/Desktop/winerymobile/img/product')

    def __str__(self):
      return self.name

class ClientUser(models.Model):
    username = models.CharField(max_length=100,unique='True')
    password = models.CharField( max_length=130,)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default='True')
    birthday = models.DateField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)


    def __str__(self):
        return self.first_name + " " + self.last_name




class Users(models.Model):
    username = models.CharField(max_length=100,unique='True')
    password = models.CharField( max_length=130,)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default='True')
    is_employee = models.BooleanField(default='False')
    birthday = models.DateField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
         return self.first_name+" "+self.last_name

class Employees(models.Model):
    user = models.OneToOneField(Users)
    company = models.ForeignKey(Company)
    is_manager = models.BooleanField(default='False')

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Cart(models.Model):
    client = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


    def __str__(self):
        return self.client.username + " " + self.product.name


class Orders(models.Model):
    date = models.DateField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    sasia=models.IntegerField()
    client=models.ForeignKey(Users)
    product = models.ForeignKey(Product)

    def __str__(self):
        return self.client.username + " " + self.product.name
