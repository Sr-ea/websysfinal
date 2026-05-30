from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import Http404
from .models import Category, Product


def custom_404(request, exception):
    return render(request, '404.html', status=404)


def custom_500(request):
    return render(request, '500.html', status=500)


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    query = request.GET.get('q', '')

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    return render(request, 'catalog/product_list.html', {
        'category': category,
        'categories': categories,
        'products': products,
        'query': query,
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id, available=True)
    related = Product.objects.filter(category=product.category, available=True).exclude(id=product_id)[:4]
    return render(request, 'catalog/product_detail.html', {
        'product': product,
        'related': related,
    })
