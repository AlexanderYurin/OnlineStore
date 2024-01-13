from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from goods.models import Categories, Products


class CatalogList(ListView):
	model = Products
	context_object_name = "products"
	template_name = "goods/catalog.html"


class ProductDetail(DetailView):
	model = Products
	template_name = "goods/product.html"
	context_object_name = "product"

