from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Product, Order

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'description', 'image', 'stock']

from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'phone_number', 'wilaya', 'commune', 'address']
        widgets = {
            'wilaya': forms.Select(attrs={'id': 'id_wilaya'}),
        }