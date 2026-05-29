from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.cart import Cart
from orders.models import Order, OrderItem
from .forms import CheckoutForm


@login_required
def checkout(request):
    cart = Cart(request)
    if len(cart) == 0:
        messages.warning(request, 'Your cart is empty.')
        return redirect('catalog:product_list')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            order = Order.objects.create(
                user=request.user,
                full_name=cd['full_name'],
                email=cd['email'],
                address=cd['address'],
                city=cd['city'],
                postal_code=cd['postal_code'],
                country=cd['country'],
                total=cart.get_total(),
                status='pending',
            )

            for item in cart:
                product = item['product']
                product.refresh_from_db()

                if not product.available or product.stock < item['quantity']:
                    order.delete()
                    messages.error(
                        request,
                        f'Not enough stock for "{product.name}". '
                        f'Only {product.stock} left in stock.'
                    )
                    return redirect('cart:cart_detail')

                OrderItem.objects.create(
                    order=order,
                    product=product,
                    product_name=product.name,
                    price=item['price'],
                    quantity=item['quantity'],
                )

                product.stock -= item['quantity']
                product.save()

            cart.clear()
            messages.success(request, 'Order placed successfully!')
            return redirect('checkout:checkout_success', order_id=order.id)
        messages.error(request, 'Please correct the errors below.')
    else:
        form = CheckoutForm(initial={
            'full_name': request.user.get_full_name() or request.user.username,
            'email': request.user.email,
        })

    return render(request, 'checkout/checkout.html', {'cart': cart, 'form': form})


@login_required
def checkout_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'checkout/checkout_success.html', {'order': order})
