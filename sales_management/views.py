from django.shortcuts import render
from django.http import HttpResponse
from account.models import Account


def home_screen_view(request):
    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts
    return render(request, 'sales_management/home.html', context)

