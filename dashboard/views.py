from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django import forms
from catalog.models import Category, Product
from catalog.forms import ProductForm
from orders.models import Order


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Category name'}),
            'slug': forms.TextInput(attrs={'placeholder': 'category-slug'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Optional description'}),
        }


@staff_member_required
def dashboard_home(request):
    low_stock = Product.objects.filter(stock__lt=5, available=True)
    context = {
        'product_count': Product.objects.count(),
        'order_count': Order.objects.count(),
        'pending_orders': Order.objects.filter(status='pending').count(),
        'recent_orders': Order.objects.order_by('-created_at')[:5],
        'low_stock_products': low_stock,
    }
    return render(request, 'dashboard/home.html', context)


@staff_member_required
def dashboard_products(request):
    query = request.GET.get('q', '')
    products = Product.objects.select_related('category').all()
    if query:
        products = products.filter(name__icontains=query)
    return render(request, 'dashboard/products.html', {'products': products, 'query': query})


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
    return render(request, 'dashboard/product_confirm_delete.html', {'product': product})


@staff_member_required
def dashboard_orders(request):
    status_filter = request.GET.get('status', '')
    orders = Order.objects.select_related('user').all()
    if status_filter:
        orders = orders.filter(status=status_filter)
    return render(request, 'dashboard/orders.html', {
        'orders': orders,
        'status_filter': status_filter,
        'order_status_choices': Order.STATUS_CHOICES,
    })


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


@staff_member_required
def dashboard_categories(request):
    categories = Category.objects.all()
    return render(request, 'dashboard/category_list.html', {'categories': categories})


@staff_member_required
def dashboard_category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.success(request, f'Category "{category.name}" created.')
            return redirect('dashboard:dashboard_categories')
        messages.error(request, 'Please correct the errors below.')
    else:
        form = CategoryForm()
    return render(request, 'dashboard/category_form.html', {'form': form, 'category': None})


@staff_member_required
def dashboard_category_edit(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, f'Category "{category.name}" updated.')
            return redirect('dashboard:dashboard_categories')
        messages.error(request, 'Please correct the errors below.')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'dashboard/category_form.html', {'form': form, 'category': category})


@staff_member_required
def dashboard_category_delete(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        name = category.name
        category.delete()
        messages.success(request, f'Category "{name}" deleted.')
        return redirect('dashboard:dashboard_categories')
    return render(request, 'dashboard/category_confirm_delete.html', {'category': category})
