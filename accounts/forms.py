import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'you@example.com',
            'autocomplete': 'email',
        })
    )
    phone_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': '+63 917 123 4567',
            'pattern': '^\\+?[0-9\\-\\s\\(\\)]+$',
            'title': 'Enter a valid mobile number',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Choose a username',
                'autocomplete': 'username',
                'minlength': '3',
            }),
        }

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number', '')
        if phone:
            cleaned = re.sub(r'[\s\-\(\)]+', '', phone)
            if not re.match(r'^\+?[0-9]{7,15}$', cleaned):
                raise forms.ValidationError(
                    'Enter a valid mobile number.'
                )
            return cleaned
        return phone
