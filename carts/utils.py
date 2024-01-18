from django.db.models.manager import BaseManager
from django.http import HttpRequest
from django.template.loader import render_to_string

from carts.models import Cart


def get_user_cart(request: HttpRequest) -> BaseManager:
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)


def get_cart_items_html(request: HttpRequest) -> str:
    cart_items_html = render_to_string(
        template_name="carts/includes/include_cart.html",
        context={"carts": get_user_cart(request)},
        request=request
    )
    return cart_items_html
