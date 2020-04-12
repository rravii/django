from django import forms
from product_management.models import Products

class CreateAddProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'company', 'type', 'cost', 'stock']