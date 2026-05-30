from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from catalog.models import Product
from .cart import Cart


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})


def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id, available=True)
    cart = Cart(request)
    try:
        quantity = int(request.POST.get('quantity', 1))
    except (TypeError, ValueError):
        quantity = 1
    if quantity > product.stock:
        messages.error(request, f'Only {product.stock} in stock.')
        return redirect(request.META.get('HTTP_REFERER', 'catalog:product_list'))
    cart.add(product, quantity)
    messages.success(request, f'{product.name} added to cart.')
    return redirect(request.META.get('HTTP_REFERER', 'catalog:product_list'))


def cart_remove(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.remove(product)
    messages.success(request, 'Item removed from cart.')
    return redirect('cart:cart_detail')


def cart_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    try:
        quantity = int(request.POST.get('quantity', 1))
    except (TypeError, ValueError):
        messages.error(request, 'Invalid quantity.')
        return redirect('cart:cart_detail')

    if quantity < 0:
        messages.error(request, 'Quantity cannot be negative.')
        return redirect('cart:cart_detail')

    if quantity > product.stock:
        messages.error(request, f'Only {product.stock} in stock.')
        return redirect('cart:cart_detail')

    if quantity > 0:
        cart.add(product, quantity, override_quantity=True)
    else:
        cart.remove(product)
    return redirect('cart:cart_detail')
