from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from Estore.models.order import Order


class OrderView(View):
    def get(self, request):
        customer_id = request.session.get('customer')
        customer_order = Order.get_orders_by_customer(customer_id)
        # print(customer_order)
        # return HttpResponse("hello")
        return render(request, 'orderview.html', {'order_prods': customer_order})
