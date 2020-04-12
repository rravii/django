from django.contrib import admin
from product_management.models import Products


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'type', 'cost', 'stock',)
    search_fields = ('name', 'type',)
    # readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Products, ProductAdmin)
