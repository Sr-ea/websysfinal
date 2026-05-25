# Agent Entry Point

All agents working on this project MUST read this file before performing any tasks. It contains the foundational mandates, technical specifications, and links to the current development plan.

# 7-Evelyn - Fruit Market Web System (Source of Truth)

## Project Overview
A fully functional fruit & grocery market website — "7-Evelyn". Users can browse products, manage a cart, and place orders. Includes an admin panel for product and order management.

## Tech Stack
- **Framework:** Django 6.0 (Python)
- **Python Version:** 3.12
- **Database:** SQLite
- **Frontend:** Django Templates + Vanilla CSS
- **Authentication:** Django's built-in auth (session-based)
- **Cart:** Session-based (anonymous users can add to cart)
- **Image Storage:** Local storage (`media/products/`)
- **Admin Panel:** Django Admin + custom dashboard for staff

## Agent Directives & Engineering Standards

### 1. Project Structure
```
websys_project/
├── market/              # Django project settings
├── accounts/            # User registration, login
├── catalog/             # Products, categories, search
├── cart/                # Session-based cart
├── checkout/            # Order placement
├── orders/              # Order history
├── dashboard/           # Staff admin panel
├── templates/           # HTML templates
├── static/              # CSS, JS, images
├── media/               # User uploads (product images)
├── manage.py            # Django management script
├── seed.py              # Database seeder
└── requirements.txt
```

### 2. Workflow Mandates
- **Research -> Strategy -> Execution:** Always validate assumptions before implementing.
- **Validation:** Every change must be verified. Run `python manage.py check` before committing.
- **Development Roadmap:** Read `DEVELOPMENT_PLAN.md` before beginning work. Update it when tasks are completed.
- **Documentation:** Update this file if the project architecture or tech stack changes.

## Core Features

### User Side (Customer)
1. **Authentication:** Register and Login (Django built-in auth).
2. **Product Catalog:** Grid view, search, filter by category, product detail.
3. **Shopping Cart:** Session-based, add/update/remove items.
4. **Checkout:** Shipping info form, order summary, order placement.
5. **Order History:** View past orders with status (Pending/Shipped/Completed).

### Admin Side (Staff)
1. **Dashboard:** Overview stats (products, orders, pending).
2. **Product Management (CRUD):** Add, edit, delete products with image upload.
3. **Order Management:** View all orders, update status.
4. **Django Admin:** Full admin interface at `/admin/`.

## Database Schema

### User (Django AbstractUser)
- username, email, password (hashed), phone_number, is_staff

### Category
- name, slug (unique), description

### Product
- name, description, price, image, category (FK), stock, available, created_at

### Order
- user (FK), full_name, email, address, city, postal_code, country, total, status, created_at

### OrderItem
- order (FK), product (FK), product_name, price, quantity

## Seed Accounts
| Role | Username | Password |
|------|----------|----------|
| Admin | admin | admin123 |
| Customer | customer | customer123 |

## Commands
```bash
pip install -r requirements.txt     # Install dependencies
python manage.py runserver          # Start dev server
python manage.py makemigrations     # Create migrations
python manage.py migrate            # Apply migrations
python seed.py                      # Seed products & test users
python manage.py createsuperuser    # Create admin
```

## Design
See `DESIGN.md` for the 7-Evelyn design system (colors, typography, spacing, components).
