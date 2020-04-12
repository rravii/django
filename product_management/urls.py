from django.urls import path
from product_management.views import *


app_name = 'product_management'

urlpatterns=[
    path('products/', create_product_view, name='product'),
]


