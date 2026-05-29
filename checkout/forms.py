from django import forms


class CheckoutForm(forms.Form):
    full_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Juan Dela Cruz',
            'autocomplete': 'name',
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'you@example.com',
            'autocomplete': 'email',
        })
    )
    address = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={
            'placeholder': '123 Rizal St, Brgy. San Jose',
            'autocomplete': 'street-address',
        })
    )
    city = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Manila',
            'autocomplete': 'address-level2',
        })
    )
    postal_code = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'placeholder': '1000',
            'autocomplete': 'postal-code',
            'pattern': '[0-9]{4,10}',
            'title': 'Enter a valid postal code (4-10 digits)',
        })
    )
    country = forms.CharField(
        max_length=100,
        initial='Philippines',
        widget=forms.TextInput(attrs={
            'autocomplete': 'country-name',
        })
    )
