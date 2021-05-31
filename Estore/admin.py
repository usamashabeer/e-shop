from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.order import Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'description')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'quantity', 'price', 'date')


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
