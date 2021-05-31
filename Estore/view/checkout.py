from django.shortcuts import render, redirect
from django.views import View
from Estore.models.order import Order
from Estore.models.product import Product
from Estore.models.customer import Customer


class Checkout(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer_id = request.session.get('customer')
        customer = Customer.get_customer_with_id(customer_id)
        cart = request.session.get('cart')
        products = Product.get_all_products_id(list(cart))

        for product in products:
            order = Order(customer=customer,
                          product=product,
                          price=product.price,
                          quantity=cart.get(str(product.id)),
                          address=address,
                          phone=phone)
            order.order_save()
        request.session['cart'] = {}
        return redirect('cart')
