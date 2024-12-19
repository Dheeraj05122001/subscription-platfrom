from django.urls import path
from .views import product_list, checkout, success, cancel

urlpatterns = [
    path('', product_list, name='product_list'),
    path('checkout/<str:stripe_product_id>/',checkout,name='checkout'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),

]