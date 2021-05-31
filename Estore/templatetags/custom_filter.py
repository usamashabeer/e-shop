from django import template

register = template.Library()


@register.filter(name='currency')
def currency(number):
    val = 'Rs. ' + str(number)
    return val


@register.filter(name='multiply')
def multiply(number, number2):
    return number * number2
