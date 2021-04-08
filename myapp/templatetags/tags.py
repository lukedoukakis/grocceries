
from django import template
from myapp.models import CartItem

register = template.Library()


@register.filter
def lookup(d, key):
    return d[key]


@register.filter
def multiply(value, arg):
    return value * arg
