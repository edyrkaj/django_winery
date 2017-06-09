from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from winery import views

urlpatterns=[

    url(r'^$', views.CompanyList.as_view(), name='index'),
    url(r'^category/$', views.CategoryList.as_view(), name='category_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.CompanyDetails.as_view(), name='company_details'),
    url(r'^(?P<pk_c>[0-9]+)/(?P<pk_cat>[0-9]+)/products/$', views.CategoryProduct.as_view(), name='category_product'),
    url(r'^clientuserspost$', views.ClientUsersPost.as_view(), name='clientpost'),# sing up nga klienti
    url(r'^employeespost$', views.EmployeesPost.as_view(), name='employeespost'),# sing up per punonjesin
    url(r'^(?P<username>[\w.@+-]+)/userslog$', views.UsersLog.as_view(), name='userslog'),
    url(r'^(?P<employee_id>[0-9]+)/employeeslog$', views.EmployeesLog.as_view(), name='employeeslog'),
    url(r'^(?P<pk_client>[0-9]+)/cart/$', views.CartList.as_view(), name='cart_list'),
    url(r'^(?P<pk_cart>[0-9]+)/cartitemdelete/$', views.CartItemDelete.as_view(), name='cart_item_delete'),
    url(r'^cartitemadd/$', views.CartItemAdd.as_view(), name='cart_item_add'),
    url(r'^orders$', views.OrdersList.as_view(), name='orders'),
    url(r'^(?P<pk_client>[0-9]+)/ordersclient$', views.OrdersClientList.as_view(), name='ordersclient'),
    url(r'^(?P<pk_company>[0-9]+)/orderscompany$', views.OrdersCompanyList.as_view(), name='orderscompany'),
    url(r'^(?P<pk_company>[0-9]+)/manageremployee$', views.ManagerEmployeeList.as_view(), name='manageremployee'),
    url(r'^(?P<prod_id>[0-9]+)/productsdelete$', views.ProductsDelete.as_view(), name='productsdelete'),
    url(r'^productsadd$', views.ProductsAdd.as_view(), name='productsadd'),

]

urlpatterns = format_suffix_patterns(urlpatterns)