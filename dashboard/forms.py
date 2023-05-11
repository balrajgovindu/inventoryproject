from django import forms
from .models import Product, Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['date','name','suppliers_name','counts','manufacturer','quantity','batch_number','expiry_date','purchase_rate','mrp_per_unit','rack']

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields =['product','order_quantity']
