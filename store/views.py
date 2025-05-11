from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from .models import Product, Order
from .forms import ProductForm, OrderForm
from .data import COMMUNES_BY_WILAYA

def home(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'store/index.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id, is_active=True)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return redirect('store:order_success')
    else:
        form = OrderForm()
    
    return render(request, 'store/detail.html', {
        'product': product,
        'form': form,
        'communes_json': json.dumps(COMMUNES_BY_WILAYA)
    })

def order_success(request):
    return render(request, 'store/order_success.html')

@login_required
def dashboard(request):
    products = Product.objects.filter(seller=request.user)
    orders = Order.objects.filter(product__seller=request.user).order_by('-created_at')
    return render(request, 'store/dashboard.html', {
        'products': products,
        'orders': orders
    })

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('store:dashboard')
    else:
        form = ProductForm()
    return render(request, 'store/product_form.html', {'form': form, 'title': 'إضافة منتج'})

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, seller=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('store:dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'store/product_form.html', {'form': form, 'title': 'تعديل منتج'})

@login_required
def toggle_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, seller=request.user)
    product.is_active = not product.is_active
    product.save()
    return redirect('store:dashboard')

@login_required
def confirm_order(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, id=order_id, product__seller=request.user)
        order.confirmed = True
        order.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order
from .forms import OrderForm

def create_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return redirect('success')  # غيّرها حسب اسم صفحة النجاح عندك
    else:
        form = OrderForm()
    return render(request, 'store/create_order.html', {'form': form, 'product': product})
