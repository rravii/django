from django.urls import path
from sales_management.views import *

app_name = "sales_management"

urlpatterns = [
    path('customer', create_customer_view, name='customer'),
]