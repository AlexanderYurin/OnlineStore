from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from goods.models import Categories


class ListCatalog(ListView):
	model = Categories
	template_name = "goods/catalog.html"
	context_object_name = "categories"


def catalog(request: HttpRequest) -> HttpResponse:
	return render(request, template_name="goods/catalog.html")


def product(request: HttpRequest) -> HttpResponse:
	return render(request, template_name="goods/product.html")