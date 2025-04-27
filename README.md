# Expense Tracker

**Expense Tracker** is a clean, responsive, personal finance web application built with Django and TailwindCSS.

It allows you to:
- Quickly add and categorize expenses.
- View expenses filtered by Today, This Month, or All Expenses.
- See dynamic summaries of spending per big category (Essentials, Groceries, Other Expenses, Stupid Expenses, etc.).
- Use the app comfortably on mobile and desktop devices.

---

## Features

- 🧮 Add expenses easily with automatic category creation.
- 📊 Dynamic summaries of total spending per major category.
- 📅 Filter expenses by Today / This Month / All.
- 📱 Mobile-first, responsive design (TailwindCSS).
- 🛠️ Future plans: Month selection, expense charts, export options.

---

## Stack

- Django 5.2
- Python 3.13
- TailwindCSS (via CDN for easy setup)
- SQLite (default for development)

---

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/expense-tracker.git
   cd expense-tracker
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

---

## Screenshots

*(Coming soon)*

---

✨ Built with love for personal finance enthusiasts.
