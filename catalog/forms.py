from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'stock', 'image', 'available']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Product name',
                'required': True,
            }),
            'description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Product description',
            }),
            'price': forms.NumberInput(attrs={
                'step': '0.01',
                'min': '0.01',
                'required': True,
            }),
            'stock': forms.NumberInput(attrs={
                'min': '0',
            }),
            'category': forms.Select(attrs={
                'required': True,
            }),
            'image': forms.FileInput(attrs={
                'accept': 'image/*',
            }),
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price <= 0:
            raise forms.ValidationError('Price must be greater than zero.')
        return price

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if not name:
            raise forms.ValidationError('Product name is required.')
        if len(name) > 200:
            raise forms.ValidationError('Product name must be 200 characters or fewer.')
        return name
