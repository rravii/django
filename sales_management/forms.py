from sales_management.models import SalesPost
from django import forms

class CreateCustomerForm(forms.ModelForm):
    class Meta:
        model = SalesPost
        fields = ['name', 'contact']