# Online Medicine Shop

![Python](https://img.shields.io/badge/Python-3.14+-blue) ![Django](https://img.shields.io/badge/Django-4.x-green) ![License](https://img.shields.io/badge/License-MIT-yellow)

A **Django-based Online Medicine Shopping System** that allows users to browse and order medicines online. Admins can manage medicines, suppliers, orders, and generate reports. Fully responsive, professional, and user-friendly.

---

## 🔹 Features

### **User Features**
- Register, login, and manage profile
- Browse/search medicines by name or category
- Add medicines to shopping cart
- Place orders and view order history
- Check order status (Pending, Completed, Delivered)

### **Admin Features**
- Manage medicines: add/edit/delete
- Maintain supplier records linked to medicines
- View all orders with total price and status
- Generate daily/monthly sales and stock reports

---

## Project Structure
OnlineMedicineProject/
│
├── medishop/ # Django project settings
├── medicines/ # Medicine app
├── users/ # User registration/login app
├── cart/ # Shopping cart app
├── orders/ # Orders app
├── reports/ # Reports app
├── templates/ # HTML templates
├── venv/ # Python virtual environment (ignored)
├── manage.py
├── README.md
└── requirements.txt

## Dependencies
Python 3.14+
Django 4.x
SQLite (default, can be changed to PostgreSQL/MySQL)
Bootstrap 5 for responsive frontend

🔗 Author
Yasir Ashaam