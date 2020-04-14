from django.shortcuts import render
from django.http import HttpResponse
from account.models import Account
from product_management.models import Products


def home_screen_view(request):
    context = {}
    accounts = Account.objects.all()
    products = Products.objects.all()
    context['accounts'] = accounts
    context['products'] = products
    return render(request, 'gui/home.html', context)

