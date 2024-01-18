from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from carts.models import Cart
from carts.utils import get_user_cart, get_cart_items_html
from goods.models import Products


def cart_add(request):
	product = Products.objects.get(id=request.POST.get("product_id"))
	if request.user.is_authenticated:
		carts = Cart.objects.filter(user=request.user, product=product)
		if carts.exists():
			cart = carts.first()
			cart.quantity += 1
			cart.save()
		else:
			Cart.objects.create(user=request.user, product=product, quantity=1)

	data = {
		"message": "Товар добавлен в корзину!",
		"cart_items_html": get_cart_items_html(request)
	}

	return JsonResponse(data)


def cart_remove(request):
	cart_id = request.POST.get("cart_id")
	cart = Cart.objects.get(id=cart_id)
	quantity_deleted = cart.quantity
	cart.delete()

	data = {
		"message": "Товар удален из корзины!",
		"cart_items_html": get_cart_items_html(request),
		"quantity_deleted": quantity_deleted
	}

	return JsonResponse(data)


def cart_change(request):
	cart_id = request.POST.get("cart_id")
	quantity = request.POST.get("quantity")
	cart = Cart.objects.filter(id=cart_id).update(quantity=quantity)

	data = {
		"message": "Товар удален из корзины!",
		"cart_items_html": get_cart_items_html(request),

	}

	return JsonResponse(data)
