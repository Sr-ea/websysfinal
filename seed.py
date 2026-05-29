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
            ('Dole Bananas', 65.00, 100, 'products/DOLEbanana.png'),
            ('Washington Red Apples', 90.00, 80, 'products/WashingtonApple.jpg'),
            ('Baguio Carrots', 55.00, 60, 'products/carrot.webp'),
            ('Fresh Tomatoes', 45.00, 75, 'products/Tomato.jpg'),
        ],
    },
    'dairy-products': {
        'name': 'Dairy Products',
        'slug': 'dairy-products',
        'description': 'Fresh dairy and chilled essentials.',
        'products': [
            ('Alaska Fresh Milk', 85.00, 50, 'products/AlaskaFreshMilk.webp'),
            ('Eden Cheese', 120.00, 40, 'products/EdenCheese.jpg'),
            ('Magnolia Butter', 95.00, 35, 'products/MagnoliaButter.png'),
            ('Nestlé Yogurt', 70.00, 45, 'products/NestleYogurt.jpg'),
        ],
    },
    'snacks': {
        'name': 'Snacks',
        'slug': 'snacks',
        'description': 'Crunchy snacks and crackers for every craving.',
        'products': [
            ('Piattos Cheese', 45.00, 90, 'products/Piattoscheese.jpg'),
            ('Nova Multigrain Snacks', 50.00, 85, 'products/Nova.webp'),
            ('SkyFlakes Crackers', 35.00, 120, 'products/Skyflakes.webp'),
            ('Rebisco Chocolate Crackers', 40.00, 100, 'products/RebiscoChoco.webp'),
        ],
    },
    'beverages': {
        'name': 'Beverages',
        'slug': 'beverages',
        'description': 'Refreshing drinks to quench your thirst.',
        'products': [
            ('Coca-Cola Mismo', 55.00, 70, 'products/CokeMismo.jpg'),
            ('Wilkins Pure Bottled Water', 25.00, 150, 'products/Wilkins water.jpg'),
            ('C2 Green Tea', 35.00, 100, 'products/c2Greentea.webp'),
            ('Zest-O Orange Juice', 40.00, 80, 'products/ZestoOrange.jpg'),
        ],
    },
    'household-essentials': {
        'name': 'Household Essentials',
        'slug': 'household-essentials',
        'description': 'Cleaning and personal care products.',
        'products': [
            ('Surf Powder Detergent', 95.00, 60, 'products/SurfPowder.webp'),
            ('Joy Dishwashing Liquid', 75.00, 55, 'products/Joy.jpg'),
            ('Safeguard Soap', 40.00, 90, 'products/Safeguard.jpg'),
            ('Palmolive Shampoo', 85.00, 65, 'products/Palmolive.jpg'),
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

    for name, price, stock, image_name in cat_data['products']:
        product, created = Product.objects.update_or_create(
            name=name,
            defaults={
                'category': cat,
                'price': price,
                'stock': stock,
                'image': image_name,
                'description': f'Fresh {name.lower()} — available at 7-Evelyn.',
            },
        )
        if created:
            print(f'    Created product: {product.name} (₱{product.price})')
        else:
            print(f'    Updated product: {product.name}')

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
