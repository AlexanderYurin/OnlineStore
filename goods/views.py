from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_list_or_404
from django.views.generic import ListView, DetailView

from goods.models import Categories, Products


class CategoryDetail(DetailView):
	model = Products
	template_name = "goods/catalog.html"
	context_object_name = "products"
	slug_url_kwarg = "cat_slug"

	def get_object(self, queryset=None):
		slug = self.kwargs.get(self.slug_url_kwarg)
		page = self.request.GET.get("page", 1)

		if slug == "all":
			queryset = Products.objects.all()
		else:
			queryset = get_list_or_404(Products.objects.filter(id_category__slug=slug))

		paginator = Paginator(queryset, 3)
		current_page = paginator.page(int(page))

		return current_page

	def get_context_data(self, **kwargs):
		context = super().get_context_data()
		context = {
			"category_slug": self.kwargs.get(self.slug_url_kwarg),
			"products": self.get_object()
		}

		return context

class ProductDetail(DetailView):
	model = Products
	template_name = "goods/product.html"
	context_object_name = "product"
