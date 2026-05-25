import os
import sys
import django

sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'market.settings')
django.setup()

from django.contrib.auth import get_user_model
from catalog.models import Category, Product

User = get_user_model()

categories = {
    'fruits-vegetables': {
        'name': 'Fruits & Vegetables',
        'slug': 'fruits-vegetables',
        'description': 'Fresh fruits and vegetables sourced daily.',
        'products': [
            ('Dole Bananas', 65.00, 100),
            ('Washington Red Apples', 90.00, 80),
            ('Baguio Carrots', 55.00, 60),
            ('Fresh Tomatoes', 45.00, 75),
        ],
    },
    'dairy-products': {
        'name': 'Dairy Products',
        'slug': 'dairy-products',
        'description': 'Fresh dairy and chilled essentials.',
        'products': [
            ('Alaska Fresh Milk', 85.00, 50),
            ('Eden Cheese', 120.00, 40),
            ('Magnolia Butter', 95.00, 35),
            ('Nestlé Yogurt', 70.00, 45),
        ],
    },
    'snacks': {
        'name': 'Snacks',
        'slug': 'snacks',
        'description': 'Crunchy snacks and crackers for every craving.',
        'products': [
            ('Piattos Cheese', 45.00, 90),
            ('Nova Multigrain Snacks', 50.00, 85),
            ('SkyFlakes Crackers', 35.00, 120),
            ('Rebisco Chocolate Crackers', 40.00, 100),
        ],
    },
    'beverages': {
        'name': 'Beverages',
        'slug': 'beverages',
        'description': 'Refreshing drinks to quench your thirst.',
        'products': [
            ('Coca-Cola Mismo', 55.00, 70),
            ('Wilkins Pure Bottled Water', 25.00, 150),
            ('C2 Green Tea', 35.00, 100),
            ('Zest-O Orange Juice', 40.00, 80),
        ],
    },
    'household-essentials': {
        'name': 'Household Essentials',
        'slug': 'household-essentials',
        'description': 'Cleaning and personal care products.',
        'products': [
            ('Surf Powder Detergent', 95.00, 60),
            ('Joy Dishwashing Liquid', 75.00, 55),
            ('Safeguard Soap', 40.00, 90),
            ('Palmolive Shampoo', 85.00, 65),
        ],
    },
}

for cat_data in categories.values():
    cat, created = Category.objects.get_or_create(
        slug=cat_data['slug'],
        defaults={'name': cat_data['name'], 'description': cat_data['description']},
    )
    if created:
        print(f'  Created category: {cat.name}')
    else:
        print(f'  Found category: {cat.name}')

    for name, price, stock in cat_data['products']:
        product, created = Product.objects.get_or_create(
            name=name,
            defaults={
                'category': cat,
                'price': price,
                'stock': stock,
                'description': f'Fresh {name.lower()} — available at 7-Evelyn.',
            },
        )
        if created:
            print(f'    Created product: {product.name} (₱{product.price})')
        else:
            print(f'    Found product: {product.name}')

admin_created = False
if not User.objects.filter(is_superuser=True).exists():
    User.objects.create_superuser('admin', 'admin@7evelyn.com', 'admin123')
    admin_created = True
    print('  Created superuser: admin / admin123')

if not User.objects.filter(username='customer').exists():
    User.objects.create_user('customer', 'customer@7evelyn.com', 'customer123')
    print('  Created test user: customer / customer123')

print('\nSeed complete!')
print(f'  Admin login:   admin / admin123')
print(f'  Customer login: customer / customer123')
