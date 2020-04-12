from django.shortcuts import render, redirect
from product_management.models import *
from product_management.forms import *
from account.models import *


def create_product_view(request):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreateAddProductsForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CreateAddProductsForm()

    context['form'] = form

    return render(request, "product_management/add_products.html", context)
