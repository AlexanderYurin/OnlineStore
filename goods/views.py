from typing import Dict

from django.core.paginator import Paginator
from django.db.models.manager import BaseManager
from django.shortcuts import get_list_or_404
from django.views.generic import ListView, DetailView

from goods.models import Categories, Products
from goods.filters import query_search


class CategoryDetail(DetailView):
	model = Products
	template_name = "goods/catalog.html"
	context_object_name = "products"
	slug_url_kwarg = "cat_slug"

	def get_object(self, queryset=None) -> BaseManager[Products]:
		query = self.request.GET.get("q")
		slug = self.kwargs.get(self.slug_url_kwarg)
		if slug == "all":
			queryset = Products.objects.all()
		elif query:
			queryset = query_search(query)
		else:
			queryset = get_list_or_404(Products.objects.filter(id_category__slug=slug))

		on_sale = self.request.GET.get("on_sale")
		order_by = self.request.GET.get("order_by")
		if on_sale:
			queryset = queryset.filter(discount__gt=0)
		if order_by and order_by != "default":
			queryset = queryset.order_by(order_by)

		page = self.request.GET.get("page", 1)

		paginator = Paginator(queryset, 3)
		current_page = paginator.page(int(page))

		return current_page

	def get_context_data(self, **kwargs) -> Dict:
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
