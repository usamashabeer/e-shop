from django.shortcuts import render, redirect
from Estore.models.product import Product
from Estore.models.category import Category
from django.views import View


# Create your view here.

class Index(View):
    def get(self, request):
        products = Product.get_all_products()
        categories = Category.get_all_category()
        data = {}
        # This category value come from URL
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_product_by_category_id(categoryID)
        # request.GET.category
        data['products'] = products
        data['category'] = categories
        if not request.session.get('cart'):
            cart = {}
            request.session['cart'] = cart

        return render(request, 'index.html', data)

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1

        else:
            cart = {product: 1}
        request.session['cart'] = cart
        print(cart)
        return redirect('/')
