from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from catalog.models import Product
from catalog.forms import ProductForm
from orders.models import Order


@staff_member_required
def dashboard_home(request):
    context = {
        'product_count': Product.objects.count(),
        'order_count': Order.objects.count(),
        'pending_orders': Order.objects.filter(status='pending').count(),
        'recent_orders': Order.objects.order_by('-created_at')[:5],
    }
    return render(request, 'dashboard/home.html', context)


@staff_member_required
def dashboard_products(request):
    products = Product.objects.select_related('category').all()
    return render(request, 'dashboard/products.html', {'products': products})


@staff_member_required
def dashboard_product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'Product "{product.name}" created.')
            return redirect('dashboard:dashboard_products')
        messages.error(request, 'Please correct the errors below.')
    else:
        form = ProductForm()

    return render(request, 'dashboard/product_form.html', {'product': None, 'form': form})


@staff_member_required
def dashboard_product_edit(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Product "{product.name}" updated.')
            return redirect('dashboard:dashboard_products')
        messages.error(request, 'Please correct the errors below.')
    else:
        form = ProductForm(instance=product)

    return render(request, 'dashboard/product_form.html', {'product': product, 'form': form})


@staff_member_required
def dashboard_product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted.')
    return redirect('dashboard:dashboard_products')


@staff_member_required
def dashboard_orders(request):
    orders = Order.objects.select_related('user').all()
    return render(request, 'dashboard/orders.html', {'orders': orders})


@staff_member_required
def dashboard_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Order.STATUS_CHOICES):
            order.status = new_status
            order.save()
            messages.success(request, f'Order {order.id} status updated to {new_status.title()}.')
    return redirect('dashboard:dashboard_orders')
