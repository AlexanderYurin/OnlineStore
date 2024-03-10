from django.db.models import QuerySet
from django.db.models.manager import BaseManager
from django.http import HttpRequest
from django.template.loader import render_to_string

from carts.models import Cart
from users.utils import get_session_key


def get_user_cart(request: HttpRequest) -> QuerySet[Cart]:
	if request.user.is_authenticated:
		return Cart.objects.filter(user=request.user).select_related("product")
	return Cart.objects.filter(session_key=get_session_key(request)).select_related("product")


def get_cart_items_html(request: HttpRequest) -> str:
	carts = get_user_cart(request)
	cart_items_html = render_to_string(
		template_name="carts/includes/include_cart.html",
		context={"carts": carts},
		request=request
	)
	return cart_items_html
