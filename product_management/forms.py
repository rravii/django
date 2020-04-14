from django import forms
from product_management.models import Products

class CreateAddProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'company', 'type', 'cost', 'stock']

class UpdateAddProductsForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = ['name', 'company', 'type', 'cost', 'stock']

    def save(self, commit=True):
        add_product = self.instance
        # add_product.id = self.cleaned_data['id']
        add_product.name = self.cleaned_data['name']
        add_product.company = self.cleaned_data['company']
        add_product.type = self.cleaned_data['type']
        add_product.cost = self.cleaned_data['cost']
        add_product.stock = self.cleaned_data['stock']

        if commit:
            add_product.save()
        return add_product




