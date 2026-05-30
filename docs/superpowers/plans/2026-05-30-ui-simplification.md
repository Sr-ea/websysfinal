# UI Simplification Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Simplify the visual aesthetic of 7-Evelyn by removing all gradients and tightening the color palette.

**Architecture:** Modifying `static/css/market.css` to replace gradient definitions with solid colors from the established theme, and adjusting CSS variables.

**Tech Stack:** CSS (Vanilla)

---

### Task 1: Update CSS Variables and Global Styles

**Files:**
- Modify: `static/css/market.css`

- [ ] **Step 1: Replace gradient definitions with solid colors**

Open `static/css/market.css` and update the variables and style definitions.

```css
/* Update Hero gradient to solid */
.hero {
  background: var(--green-900);
  color: var(--white);
  text-align: center;
  padding: 60px 20px;
}

/* Update category placeholders to solid colors */
.cat-fruits-vegetables { background: var(--green-700); }
.cat-dairy-products { background: #2c5f8a; }
.cat-snacks { background: var(--orange-600); }
.cat-beverages { background: #6d28d9; }
.cat-household-essentials { background: var(--gray-700); }
```

- [ ] **Step 2: Commit**

```bash
git add static/css/market.css
git commit -m "style: remove gradients and set solid colors"
```

---

### Task 2: Verify Consistency and Cleanup

**Files:**
- Modify: `static/css/market.css`

- [ ] **Step 1: Review for lingering gradients**

Scan `static/css/market.css` for any other `linear-gradient` occurrences and ensure they are converted to solid colors as needed.

- [ ] **Step 2: Verify UI**

Run the local development server: `python manage.py runserver` and manually verify that hero sections and placeholders now use solid colors.

- [ ] **Step 3: Commit**

```bash
git add static/css/market.css
git commit -m "style: finalize gradient removal"
```
