from django.contrib import admin
from sales_management.models import SalesPost


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact', 'date_purchase',)
    search_fields = ('name',)
    readonly_fields = ('date_purchase',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(SalesPost, ProductAdmin)
