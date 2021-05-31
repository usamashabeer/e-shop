from django.shortcuts import redirect, render
from django.views import View
from Estore.models.product import Product


class CartView(View):
    def get(self, request):
        cart = request.session.get('cart')
        if cart:
            cart_prods = Product.get_all_products_id(list(cart))
        else:
            cart_prods = False
        return render(request, 'cartview.html', {'cart_prods': cart_prods})
