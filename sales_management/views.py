from django.shortcuts import render,redirect
from sales_management.models import *
from sales_management.forms import *
from account.models import Account


def create_customer_view(request):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreateCustomerForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        obj.author = author
        obj.save()
        form = CreateCustomerForm()

    context['form'] = form

    return render(request, 'sales_management/sales_home.html', context)
