from django.contrib import admin
from .models import Category, Supplier, Medicine

admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Medicine)