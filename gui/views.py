from django.shortcuts import render
from django.http import HttpResponse
from account.models import Account
from product_management.models import Products
from product_management.views import get_product_queryset
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

PRODUCTS_PER_PAGE = 5

def home_screen_view(request, *args, **kwargs):
    context = {}

    query = ""
    if request.GET:
        query = request.GET.get('q', '')
        context['query'] = str(query)

    accounts = Account.objects.all()
    # products = Products.objects.all()
    product = get_product_queryset(query)
    # context['products'] = products

    # Pagination
    page = request.GET.get('page', 1)
    product_paginator = Paginator(product, PRODUCTS_PER_PAGE)

    try:
        product = product_paginator.page(page)
    except PageNotAnInteger:
        product = product_paginator.page(PRODUCTS_PER_PAGE)
    except EmptyPage:
        product = product_paginator.page(product_paginator.num_pages)

    context['product'] = product

    # Pagination
    page = request.GET.get('page', 1)
    accounts_paginator = Paginator(accounts, PRODUCTS_PER_PAGE)

    try:
        accounts = accounts_paginator.page(page)
    except PageNotAnInteger:
        accounts = accounts_paginator.page(PRODUCTS_PER_PAGE)
    except EmptyPage:
        accounts = accounts_paginator.page(accounts_paginator.num_pages)

    context['accounts'] = accounts

    return render(request, 'gui/home.html', context)

