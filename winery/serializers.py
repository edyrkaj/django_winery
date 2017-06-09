from __future__ import unicode_literals

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import CharField

from .models import Category, Company, Product, ClientUser, Cart, Employees, Users, Orders


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields = '__all__'  #fields = '__all__'

class ClientUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientUser
        fields = '__all__'

class CartSerializerDetails(serializers.ModelSerializer):


    name = serializers.CharField(source='product.name', read_only=True)
    price = serializers.DecimalField(source='product.price', read_only=True,max_digits=8, decimal_places=2)
    company = serializers.CharField(source='product.company.name',read_only=True)
    image = serializers.FileField( source='product.image',read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'


class OrdersSerializer(serializers.ModelSerializer):
    company = serializers.CharField(source='product.company.name', read_only=True)
    name = serializers.CharField(source='product.name', read_only=True)
    client_name=serializers.CharField(source='client.first_name', read_only=True)
    client_surname=serializers.CharField(source='client.last_name', read_only=True)
    class Meta:
        model = Orders
        fields = '__all__'

class ManagerEmployeeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    address=serializers.CharField(source='user.address', read_only=True)
    city=serializers.CharField(source='user.city', read_only=True)
    phone_number=serializers.CharField(source='user.phone_number', read_only=True)
    class Meta:
        model = Employees
        fields = '__all__'



