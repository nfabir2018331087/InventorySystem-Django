from django import forms
from .models import Product
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Password didn't match!") 
        return cleaned_data
    


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_id' : 'Product ID',
            'name' : 'Name',
            'sku' : 'SKU',
            'price' : 'Price',
            'quantity' : 'Quantity',
            'supplier' : 'Supplier',
        }
        widgets = {
            'product_id' : forms.NumberInput(attrs={'placeholder' : 'e.g. 1', 'class' : 'form-control'}),
            'name' : forms.TextInput(attrs={'placeholder' : 'e.g. ABC', 'class' : 'form-control'}),
            'sku' : forms.TextInput(attrs={'placeholder' : 'e.g. X123', 'class' : 'form-control'}),
            'price' : forms.NumberInput(attrs={'placeholder' : 'e.g. 1.0', 'class' : 'form-control'}),
            'quantity' : forms.NumberInput(attrs={'placeholder' : 'e.g. 1', 'class' : 'form-control'}),
            'supplier' : forms.TextInput(attrs={'placeholder' : 'e.g. XYZ Org', 'class' : 'form-control'}),
        }