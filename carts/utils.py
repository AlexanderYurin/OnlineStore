from django.db.models.manager import BaseManager
from django.http import HttpRequest
from django.template.loader import render_to_string

from carts.models import Cart
from users.utils import get_session_key


def get_user_cart(request: HttpRequest) -> BaseManager:
	if request.user.is_authenticated:
		return Cart.objects.filter(user=request.user)
	return Cart.objects.filter(session_key=get_session_key(request))


def get_cart_items_html(request: HttpRequest) -> str:
	cart_items_html = render_to_string(
		template_name="carts/includes/include_cart.html",
		context={"carts": get_user_cart(request)},
		request=request
	)
	return cart_items_html
