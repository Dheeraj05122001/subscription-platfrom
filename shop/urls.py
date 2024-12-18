from django.urls import path
from .views import product_list, checkout, success, cancel,add_product

urlpatterns = [
    path('', product_list, name='product_list'),
    path('checkout/<int:product_id>/', checkout, name='checkout'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),
    path('add products/',add_product,name='add product')
]