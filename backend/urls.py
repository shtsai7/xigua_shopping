from django.urls import path

from . import views

app_name = 'backend'
urlpatterns = [
    path('', views.index, name='index'),
    path('customer/', views.CustomerView.as_view(), name='customer'),
    path('customer/<int:customer_id>/', views.customerdetail, name='customer_detail'),
    path('product/', views.product, name='product'),
    path('product/<int:product_id>/', views.productdetail, name='product_detail'),
    path('order/', views.order, name='order'),
    path('order/<int:order_id>/', views.orderdetail, name='order_detail'),
    path('inventory/', views.inventory, name='inventory'),
    path('inventory/<int:inventory_id>', views.inventorydetail, name='inventory_detail'),
    path('newshoppingcart/', views.newshoppingcart, name='newshoppingcart'),
    path('shoppingcart/<int:order_id>', views.shoppingcart, name='shoppingcart'),
    path('addtocart/', views.addtocart, name='addtocart'),
    path('removefromcart/', views.removefromcart, name='removefromcart'),
    path('selectcustomer/', views.selectcustomer, name='selectcustomer'),
    path('setcustomer/', views.setcustomer, name='setcustomer'),
    path('addpayment/', views.addpayment, name='addpayment'),
    path('addshipping/', views.addshipping, name='addshipping'),
    path('addcustomer/', views.addcustomer, name='addcustomer'),
    path('updatecustomer/', views.updatecustomer, name='updatecustomer'),
]
