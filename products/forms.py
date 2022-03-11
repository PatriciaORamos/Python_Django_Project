from django import forms
from . import models

class CreateProduct(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = ['title', 'category', 'description', 'price', 'quantity', 'sku', 'picture']