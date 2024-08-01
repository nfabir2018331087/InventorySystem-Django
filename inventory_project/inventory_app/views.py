from django.shortcuts import render, redirect
from .forms import ProductForm, RegistrationForm
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User


# Create your views here.

# authentication views
def register_view(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = User.objects.create_user(username=username, password=password, email=email)
            login(request, user)
            return redirect('home')
        
    return render(request, 'accounts/registration.html', {'form': form})


def login_view(request):
    error_msg = None
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            error_msg = "Invalid Credentials!"

    return render(request, 'accounts/login.html', {'error': error_msg})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        # return redirect('home')
        return render(request, 'accounts/logout.html')
    # return render(request, 'accounts/logout.html')
    

# home view
@login_required
def home_view(request):
    return render(request, 'home.html')

# contact view
@login_required
def contact_view(request):
    return render(request, 'contact.html')

# CRUD

# create view
@login_required
def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    
    return render(request, 'create_product.html', {'form': form})

# read view
@login_required
def products_view(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

# update view
@login_required
def product_update_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    return render(request, 'create_product.html', {'form': form})

# delete view
@login_required
def product_delete_view(request, product_id):
    product = Product.objects.get(product_id = product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    return render(request, 'prod_delete_confirmation.html', {'product': product})