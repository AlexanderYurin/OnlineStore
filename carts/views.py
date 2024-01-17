from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from carts.models import Cart
from goods.models import Products


def cart_add(request, product_slug):
	product = Products.objects.get(slug=product_slug)
	if request.user.is_authenticated:
		carts = Cart.objects.filter(user=request.user, product=product)
		if carts.exists():
			cart = carts.first()
			cart.quantity += 1
			cart.save()
		else:
			Cart.objects.create(user=request.user, product=product, quantity=1)
	return redirect(request.META["HTTP_REFERER"])


def cart_remove(request, cart_id):
	cart = Cart.objects.get(id=cart_id)
	cart.delete()

	return redirect(request.META["HTTP_REFERER"])


