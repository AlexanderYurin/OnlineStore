from django import template

from carts.utils import get_user_cart

register = template.Library()


@register.simple_tag
def carts_user(request):
	return get_user_cart(request)
