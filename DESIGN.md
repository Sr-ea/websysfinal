# 7-Evelyn Fruit Market — Design System

## Overview
7-Evelyn is a fresh fruit & grocery market with a warm, earthy aesthetic. The design uses a green-based palette (freshness, produce) accented with warm oranges (citrus, energy) against a cream background.

## Colors

### Primary
- `--green-900` `#1a3a2a` — Deep forest (navbar, footer, headings)
- `--green-700` `#2d6a4f` — Buttons, primary actions
- `--green-500` `#40916c` — Accents, tags, success states
- `--green-300` `#74c69d` — Secondary accents, nav links
- `--green-100` `#d8f3dc` — Success message backgrounds

### Accent (Warm / Citrus)
- `--orange-600` `#e76f51` — Price text, hover states
- `--orange-500` `#f4a261` — "Add to Cart" buttons, hero accent
- `--orange-200` `#fdf0d5` — Warning/pending backgrounds

### Neutrals
- `--cream` `#fefae0` — Page background
- `--white` `#ffffff` — Card backgrounds
- `--gray-100` to `--gray-900` — Text hierarchy & borders

### Semantic
- `--red-500` `#d62828` — Danger, out-of-stock, delete
- Green-100 — Success backgrounds
- Orange-200 — Pending/warning backgrounds

## Typography
- **Font stack:** `'Segoe UI', system-ui, -apple-system, sans-serif`
- **Headings:** 700–800 weight, green-900
- **Body:** 400 weight, gray-900
- **Prices:** 700 weight, orange-600

## Spacing
- Base unit: 4px
- Standard padding: 20px (container), 16px (card content), 32px (sections)
- Grid gap: 24px (desktop), 12px (mobile)

## Components

### Navbar
- Background green-900, white text, sticky top
- Brand: "7-Evelyn" with cart emoji
- Links: Home, Cart (with badge), Orders, Admin, Login/Logout

### Hero
- Gradient green-900 → green-500
- White title with orange accent span
- Search bar with orange submit button

### Product Cards
- White background, subtle shadow, hover lift
- Square image area (gray-100 placeholder if no image)
- Category tag (green-500, uppercase), name, price (orange-600), stock badge
- Full-width orange "Add to Cart" button

### Buttons
- `.btn-primary` — green-700 background, white text
- `.btn-cart` — orange-500 background (add to cart)
- `.btn-outline` — green-700 border, transparent bg
- `.btn-danger` — red-500 background

### Forms
- White card with shadow
- 2px border, green-500 focus state
- Full-width submit buttons

### Dashboard (Admin)
- Sidebar: green-900 with green-300 links
- Main: gray-100 background
- Stats cards: white, centered number + label
- Tables: white, striped hover rows

## Dark Mode

The site includes a fully supported dark mode toggle (🌙/☀️) in the navbar. Preference is persisted via `localStorage` and falls back to the OS `prefers-color-scheme` setting. The `<html>` element gets `data-theme="dark"` when active.

### Overridden Variables (`[data-theme="dark"]`)
- `--cream` — `#121212` (page background)
- `--white` — `#1e1e1e` (card backgrounds)
- `--gray-100` — `#2a2a2a`
- `--gray-200` — `#333333`
- `--gray-300` — `#444444`
- `--gray-500` — `#999999`
- `--gray-700` — `#cccccc`
- `--gray-900` — `#e0e0e0`
- `--shadow-sm` / `--shadow-md` — Darker shadow values

### Elements forced to `#ffffff` in dark mode
- Navbar brand ("7-Evelyn")
- Hero title and orange-accented span
- Section titles ("All Products")
- Category pill text on hover/active

### Category pills in dark mode
- **Default:** White background (`#f8f9fa`), black text (`#212529`) — same as light mode
- **Hover/Active:** Green background (`var(--green-700)`), white text

## Responsive
- **Desktop:** 3-4 column product grid
- **Tablet:** 2-column grid, stacked checkout
- **Mobile:** 1-column, collapsed nav, stacked layout
