from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from catalog.models import Category, Product
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
    categories = Category.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        stock = request.POST.get('stock', 0)
        image = request.FILES.get('image')

        product = Product.objects.create(
            name=name,
            description=description,
            price=price,
            category_id=category_id,
            stock=stock,
            image=image,
        )
        messages.success(request, f'Product "{name}" created.')
        return redirect('dashboard:dashboard_products')

    return render(request, 'dashboard/product_form.html', {'categories': categories, 'product': None})


@staff_member_required
def dashboard_product_edit(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()
    if request.method == 'POST':
        product.name = request.POST.get('name', product.name)
        product.description = request.POST.get('description', product.description)
        product.price = request.POST.get('price', product.price)
        product.category_id = request.POST.get('category', product.category_id)
        product.stock = request.POST.get('stock', product.stock)
        if request.FILES.get('image'):
            product.image = request.FILES['image']
        product.save()
        messages.success(request, f'Product "{product.name}" updated.')
        return redirect('dashboard:dashboard_products')

    return render(request, 'dashboard/product_form.html', {'categories': categories, 'product': product})


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
