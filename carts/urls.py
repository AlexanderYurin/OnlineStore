from django.urls import path

from carts.views import cart_add, cart_remove

app_name = "carts"


urlpatterns = [
	path("cart_remove/<int:cart_id>", cart_remove, name="cart_remove"),
	path("cart_add/<slug:product_slug>", cart_add, name="cart_add"),
	# path("cart_change/<id:cart_id>", name="cart_change"),
]
