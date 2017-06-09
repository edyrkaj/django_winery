from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import AllowAny

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


from winery.models import Company, Product, Category, ClientUser, Cart, Users, Employees, Orders
from winery.serializers import CompanySerializer, ProductSerializer, CategorySerializer, ClientUserSerializer, \
    CartSerializer, CartSerializerDetails, UsersSerializer, EmployeesSerializer, OrdersSerializer, \
    ManagerEmployeeSerializer


class CompanyList(APIView):

    def get(self, request, format=None):
        companys = Company.objects.all()
        serializer = CompanySerializer(companys, many=True)
        return Response(serializer.data)



class CompanyDetails(APIView):

    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)


class ProductsAdd(APIView):

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class ProductsDelete(APIView):

    def get(self, request,prod_id, format=None):
        product = Product.objects.get(pk=prod_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def delete(self, request, prod_id, format=None):
        product = Product.objects.get(pk=prod_id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class CategoryList(APIView):

    def get(self, request, format=None):
        categorys = Category.objects.all()
        serializer = CategorySerializer(categorys, many=True)
        return Response(serializer.data)



class CategoryProduct(APIView):

    def get(self, request, pk_c , pk_cat, format=None):

        if pk_cat == '0':

            company = Company.objects.get(pk=pk_c)
            company_prod = company.product_set.all()
            serializer = ProductSerializer(company_prod, many=True)
            return Response(serializer.data)

        else :

            prod=Product.objects.filter(company=pk_c,category=pk_cat)
            if len(prod) ==0:
                return Response('Nuk ekziston nje prod me kete kategori')
            else :
                serializer = ProductSerializer(prod,many=True)
                return Response(serializer.data)

class ClientUserPost(APIView):##########

    def post(self, request, format=None):

        serializer = ClientUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientUserLog(APIView):##########

    def get_object(self, username):
        try:
            return ClientUser.objects.get(username=username)
        except ClientUser.DoesNotExist:
            raise Http404


    def get(self, request,username,format=None):
        clientuser = self.get_object(username)
        serializer = ClientUserSerializer(clientuser)
        return Response(serializer.data)


class CartList(APIView):

    def get(self, request,pk_client,format=None):
        cart = Cart.objects.filter(client=pk_client)
        serializer = CartSerializerDetails(cart, many=True)
        return Response(serializer.data)


class CartItemDelete(APIView):

    def get(self, request,pk_cart,format=None):
        cart = Cart.objects.get(pk=pk_cart)
        serializer = CartSerializerDetails(cart)
        return Response(serializer.data)

    def delete(self, request,pk_cart,format=None):
        cart = Cart.objects.get(pk=pk_cart)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CartItemAdd(APIView):

    def get(self, request,format=None):
        cart = Cart.objects.all()
        serializer = CartSerializer(cart,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersLog(APIView):

    def get_object(self, username):
        try:
            return Users.objects.get(username=username)
        except Users.DoesNotExist:
            raise Http404


    def get(self, request,username,format=None):
        users = self.get_object(username)
        serializer = UsersSerializer(users)
        return Response(serializer.data)

    def delete(self, request,username,format=None):
        user = Users.objects.get(username=username)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EmployeesLog(APIView):

    def get_object(self, employee_id):
        try:
            return Employees.objects.get(user=employee_id)
        except Employees.DoesNotExist:
            raise Http404


    def get(self, request,employee_id,format=None):
        employees = self.get_object(employee_id)
        serializer = EmployeesSerializer(employees)
        return Response(serializer.data)

    def delete(self, request,employee_id,format=None):
        employee = Employees.objects.get(user=employee_id)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ClientUsersPost(APIView):

    def get(self, request,format=None):
        clientusers = Users.objects.all()
        serializer = UsersSerializer(clientusers,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeesPost(APIView):

    def get(self, request,format=None):
        employees = Employees.objects.all()
        serializer = EmployeesSerializer(employees,many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        serializer = EmployeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrdersList(APIView):

    def get(self, request, format=None):
        orders = Orders.objects.all()
        serializer = OrdersSerializer(orders, many=True)
        return Response(serializer.data) ########


    def post(self, request, format=None):
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrdersClientList(APIView):

    def get(self, request,pk_client, format=None):
        ordersclient = Orders.objects.filter(client=pk_client)
        serializer = OrdersSerializer(ordersclient, many=True)
        return Response(serializer.data)

class OrdersCompanyList(APIView):

    def get(self, request,pk_company, format=None):
        orderscompany = Orders.objects.filter(product__company=pk_company)
        serializer = OrdersSerializer(orderscompany, many=True)
        return Response(serializer.data)


class ManagerEmployeeList(APIView):

    def get(self, request,pk_company, format=None):
        employee = Employees.objects.filter(company=pk_company,is_manager=False)
        serializer = ManagerEmployeeSerializer(employee, many=True)
        return Response(serializer.data)






