from django.shortcuts import render, redirect, get_object_or_404
from product_management.models import *
from product_management.forms import *
from account.models import *


def create_product_view(request):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    if request.POST:
        form = CreateAddProductsForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            context['create_product_view_form'] = form
    else:
            form = CreateAddProductsForm()
            context['create_product_view_form'] = form

    return render(request, "product_management/add_products.html", context)

def edit_product_view(request, slug):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    add_product = get_object_or_404(Products, slug=slug)
    if request.POST:
        form = UpdateAddProductsForm(request.POST or None, instance=add_product)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = 'Updated'
            add_product = obj

    form = UpdateAddProductsForm(
            initial={
                    'name': add_product.name,
                    'company': add_product.company,
                    'type': add_product.type,
                    'cost': add_product.cost,
                    'stock': add_product.stock,
            }
         )

    context['form'] = form
    return render(request, 'product_management/edit_product.html', context)

def delete_product_view(request, slug):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    add_product = get_object_or_404(Products, slug=slug)
    if request.POST:
        form = UpdateAddProductsForm(request.POST , instance=add_product)
        add_product.delete()
        context['success_message'] = 'Deleted Successfully'

    form = UpdateAddProductsForm(
            initial={
                'id': add_product.id,
                'name': add_product.name,
                'company': add_product.company,
                'type': add_product.type,
                'cost': add_product.cost,
                'stock': add_product.stock,
            }
        )

    context['form'] = form
    return render(request, 'product_management/delete_product.html', context)