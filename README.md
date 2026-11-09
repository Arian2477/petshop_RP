# 🛒 Pet Shop — Django Online Store

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0-092E20?logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?logo=bootstrap&logoColor=white)

A Persian-language online pet shop built with Django, with a product catalog, shopping cart, orders, user accounts and online payment.

## ✨ Features

- **Products**: categories and sub-categories, weight options, discounts, comments, search, and rich-text (CKEditor) descriptions
- **Cart**: session-based cart
- **Orders**: checkout form and order management in the admin
- **Payment**: Zarinpal gateway integration (prices in Toman, sent to the gateway in Rial)
- **Accounts**: sign-up, login, email confirmation and password reset with django-allauth
- **Localisation**: Persian UI (`fa`) and English, Jalali dates, Persian digits, translations managed with Rosetta

## 🧱 Tech stack

Django 5 · MySQL · django-allauth · django-crispy-forms (Bootstrap 5) · django-ckeditor · django-jalali-date · django-rosetta · environs

## 🗂️ Apps

| App | Purpose |
|---|---|
| `accounts` | Custom user model and forms |
| `pages` | Home, About and search pages |
| `products` | Catalog, categories, discounts and comments |
| `cart` | Shopping cart |
| `orders` | Checkout and orders |
| `payment` | Zarinpal payment flow |
| `persian_translate` | Template tags for Persian numbers and text |

## 🚀 Getting started

```bash
python -m venv venv
venv\Scripts\activate          # macOS/Linux: source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```ini
DJANGO_SECRET_KEY=change-me
DATABASE_NAME=petshop
DATABASE_USER=root
DATABASE_PASS=your-password
```

Create the MySQL database, then run:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open <http://127.0.0.1:8000/>. The admin panel is at `/admin/`.
