# Development Plan: 7-Evelyn Fruit Market

## Phase 1: Project Setup & Foundation
- [x] Wipe old MERN stack (client/, server/).
- [x] Install Python 3.12 + Django dependencies.
- [x] Install Django 6.0 + Pillow.
- [x] Scaffold Django project (`market`) and apps.
- [x] Configure SQLite database.
- [x] Create `.gitignore` for Python/Django.

## Phase 2: Database Models & Admin
- [x] Create User model (extends AbstractUser with phone_number).
- [x] Create Category model.
- [x] Create Product model.
- [x] Create Order + OrderItem models.
- [x] Register all models with Django Admin.
- [x] Seed database with 5 categories and 20 products (7-Evelyn inventory).

## Phase 3: Templates & Frontend
- [x] Create base template with nav bar.
- [x] Build product grid catalog with search and category filters.
- [x] Build product detail page.
- [x] Build cart page (session-based).
- [x] Build checkout page with shipping form.
- [x] Build order history and order detail pages.
- [x] Build auth pages (login, register).
- [x] Build admin dashboard (overview, products, orders).
- [x] Create fruit-market CSS design system.

## Phase 4: Core User Features
- [x] Product Catalog with category filtering.
- [x] Product search.
- [x] Session-based shopping cart (add, update, remove).
- [x] Checkout simulation (shipping info, order summary).
- [x] Order history and detail view.
- [x] User registration and login.

## Phase 5: Admin Panel
- [x] Dashboard overview (stats).
- [x] Product management (CRUD with image upload).
- [x] Order management (list all orders, update status).
- [x] Django Admin interface at `/admin/`.

## Phase 6: Polishing & Validation
- [x] Client/server form validation enhancements.
- [x] Final UI/UX pass: loading states & error handling.
- [x] Add product images (placeholder or actual uploads).
- [x] Responsive design verification.
- [x] Prepare documentation.

## Phase 7: Stock & Inventory
- [x] Decrement product stock on checkout (with insufficient stock handling).

## Phase 8: Dark Mode & Quality
- [x] Create `media/products/` directory with 20 placeholder product images.
- [x] Implement light/dark mode toggle (CSS custom properties + `data-theme` + localStorage persistence).
- [x] Add theme toggle button (sun/moon) in navbar with system preference detection.
- [x] Write 37 unit tests across all 6 apps (models, views, cart logic).
