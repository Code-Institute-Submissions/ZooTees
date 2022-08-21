"""products forms"""
from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    """Product Form"""
    class Meta:
        model = Product
        fields = '__all__'
