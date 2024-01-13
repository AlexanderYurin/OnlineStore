from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_list_or_404
from django.views.generic import ListView, DetailView

from goods.models import Categories, Products


class CategoryDetail(DetailView):
	model = Products
	template_name = "goods/catalog.html"
	slug_url_kwarg = "cat_slug"
	context_object_name = "products"

	def get_object(self, queryset=None):
		slug = self.kwargs.get(self.slug_url_kwarg)




		if slug == "all":
			queryset = Products.objects.all()
		else:
			queryset = get_list_or_404(Products.objects.filter(id_category__slug=slug))

		return queryset

class ProductDetail(DetailView):
	model = Products
	template_name = "goods/product.html"
	context_object_name = "product"
