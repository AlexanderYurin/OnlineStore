from abc import ABC, abstractmethod

from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline
from django.db.models.manager import BaseManager

from goods.models import Products


class ProductSearch(ABC):
	def __init__(self, query: str):
		self.query = query

	@abstractmethod
	def search(self):
		pass


class ProductSearchID(ProductSearch):
	"""Поиск по id продукта"""
	def search(self) -> BaseManager[Products]:
		return Products.objects.filter(id=int(self.query))


class ProductSearchTitle(ProductSearch):
	"""Поиск по Title и Description продукта"""
	def search(self) -> BaseManager[Products]:
		vector = SearchVector("title", "description")
		query = SearchQuery(self.query)
		queryset = Products.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")
		queryset = queryset.annotate(headline=SearchHeadline(
			"title", query, start_sel="<span style='background-color: yellow;'>", stop_sel="</span>")).all()
		queryset = queryset.annotate(bodyline=SearchHeadline(
			"description", query, start_sel="<span style='background-color: yellow;'>", stop_sel="</span>")).all()

		return queryset


def query_search(query: str) -> BaseManager[Products] | None:
	if query.isdigit() and len(query) <= 5:
		return ProductSearchID(query).search()
	return ProductSearchTitle(query).search()
