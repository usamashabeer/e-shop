from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for key in keys:
        if key == str(product.id):
            return True
    return False


@register.filter(name='quantity')
def quantity(product, cart):
    return cart[str(product.id)]


@register.filter(name='price_quantity')
def price_quantity(product, cart):
    return cart[str(product.id)] * product.price


@register.filter(name='total_price')
def total_price(products, cart):
    sum = 0
    for product in products:
        sum += price_quantity(product, cart)
        # print(price_quantity(product, cart))
    return sum


@register.filter(name='currency')
def currency(product):
    val = ' Rs'
    return val
