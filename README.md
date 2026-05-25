# 7-Evelyn 🛒

A fruit market & grocery web application built with Django.

## Quick Start

```bash
pip install -r requirements.txt    # Install dependencies
python manage.py migrate           # Apply migrations
python seed.py                     # Seed products & test users
python manage.py runserver         # Start the server
```

Visit **http://127.0.0.1:8000** to start shopping.

## Seed Accounts

| Role | Username | Password |
|------|----------|----------|
| Admin | admin | admin123 |
| Customer | customer | customer123 |

## Features

- **Catalog** — Browse 20+ products across 5 categories (Fruits & Vegetables, Dairy, Snacks, Beverages, Household Essentials)
- **Search & Filter** — Search by name, filter by category
- **Shopping Cart** — Session-based, add/update/remove items
- **Checkout** — Shipping info form with order summary
- **Order History** — View past orders with status tracking
- **Admin Dashboard** — Manage products, update order status

## Tech Stack

- **Django 6.0** (Python 3.12)
- **pip** — Python package manager
- **SQLite** — Database
- **Vanilla CSS** — No frameworks

## Project Structure

```
market/              # Django project settings
accounts/            # Auth (register, login, logout)
catalog/             # Products, categories, search
cart/                # Session-based cart logic
checkout/            # Order placement
orders/              # Order history
dashboard/           # Staff admin panel
templates/           # HTML templates
static/              # CSS
media/               # Product image uploads
seed.py              # Database seeder
```
