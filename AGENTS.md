# Agent Entry Point

All agents working on this project MUST read this file before performing any tasks. It contains the foundational mandates, technical specifications, and links to the current development plan. Refer to `DESIGN.md` for the design system (colors, typography, spacing, components).

# E-Commerce Web System - Project Specification (Source of Truth)

## Project Overview
A fully functional basic e-commerce website allowing users to browse products, manage a cart, and simulate checkout. Includes an admin panel for product and order management.

## Tech Stack
- **Frontend:** React (TypeScript) with Vite
- **Styling:** Vanilla CSS (Modern CSS features, no Tailwind unless requested)
- **Backend:** Node.js with Express
- **Database:** MongoDB
- **Package Manager:** pnpm
- **Authentication:** JWT (JSON Web Tokens)
- **Image Storage:** Local storage (public/uploads) or Cloudinary

## Agent Directives & Engineering Standards
*These rules are foundational mandates for all agents working on this repository.*

### 1. Architectural Consistency
- **Composition over Inheritance:** Prioritize explicit composition and delegation patterns. Avoid complex prototype manipulation or deep inheritance trees.
- **Surgical Changes:** Minimize diff size by making targeted edits. Avoid unrelated refactoring or "cleanup" unless explicitly requested.
- **Type Safety:** Maintain strict TypeScript typing. Do not use `any` or suppress linter/compiler warnings.

### 2. File Structure & Organization
- **Separation of Concerns:** Keep business logic in the backend (`/server`) and UI/UX in the frontend (`/client`).
- **Standardized Folders:**
  - `client/src/components`: UI components.
  - `client/src/pages`: Top-level page components.
  - `server/models`: Mongoose schemas.
  - `server/routes`: API endpoints.
  - `server/controllers`: Request handlers.

### 3. Workflow Mandates
- **Research -> Strategy -> Execution:** Always validate assumptions before implementing.
- **Validation:** Every change must be verified. Run relevant tests or verify manually via shell if tests aren't available yet.
- **Development Roadmap:** All agents MUST read `DEVELOPMENT_PLAN.md` before beginning work. When a task is completed, the agent MUST update `DEVELOPMENT_PLAN.md` by marking the corresponding item as complete.
- **Documentation:** Update this file if the project architecture or tech stack changes.
- **UI Component Library:** Use Redis as the data/store layer when building the UI component library.

## Core Features

### User Side (Customer)
1.  **Authentication:** Register and Login.
2.  **Product Catalog:**
    *   View available products (Grid/List).
    *   Search and filter (by category, price, etc.).
    *   View detailed product information.
3.  **Shopping Cart:**
    *   Add items to cart.
    *   Update quantities or remove items.
    *   Persistent cart (via database or localStorage).
4.  **Checkout:**
    *   Checkout simulation (shipping info, order summary).
    *   *Note: Payment integration is NOT required.*
5.  **Order History:** View status and history of previous orders.

### Admin Side
1.  **Admin Login:** Secure authentication for admin users.
2.  **Product Management (CRUD):**
    *   Create, Read, Update, Delete products.
    *   Upload product images.
    *   Manage categories.
3.  **Order Management:**
    *   View all customer orders.
    *   Update order status (Pending, Completed, Shipped).

## Database Schema (MongoDB Collections)

### Users
- `_id`: ObjectId
- `name`: String
- `email`: String (Unique)
- `password`: String (Hashed)
- `isAdmin`: Boolean
- `createdAt`: Date

### Products
- `_id`: ObjectId
- `name`: String
- `description`: String
- `price`: Number
- `image`: String (URL)
- `category`: String
- `countInStock`: Number
- `createdAt`: Date

### Orders
- `_id`: ObjectId
- `user`: ObjectId (Ref: User)
- `orderItems`: Array
    - `name`: String
    - `qty`: Number
    - `image`: String
    - `price`: Number
    - `product`: ObjectId (Ref: Product)
- `shippingAddress`: Object (Address, City, PostalCode, Country)
- `totalPrice`: Number
- `status`: String (Pending, Completed, Shipped)
- `createdAt`: Date

## Interface & UI/UX Requirements
- **Responsive Design:** Mobile-friendly layouts.
- **Clean Aesthetic:** Consistent color scheme and typography.
- **Navigation:** Functional and intuitive navigation bar.
- **Feedback:** Loading states, success/error messages for forms.

## Development Workflow
- **Frontend:** `./client`
- **Backend:** `./server`
- **Environment Variables:** Use `.env` files for secrets (Mongo URI, JWT Secret).
- **Validation:** Client-side and server-side form validation.
