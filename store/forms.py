from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Product, Order

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')

# forms.py
from django import forms
from .models import Product, ProductImage

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'description', 'main_image', 'stock']

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']

ProductImageFormSet = forms.inlineformset_factory(
    Product, ProductImage, form=ProductImageForm,
    extra=3, can_delete=True, can_delete_extra=True
)
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'phone_number', 'wilaya', 'commune', 'address']
        widgets = {
            'wilaya': forms.Select(attrs={'id': 'id_wilaya'}),
        }