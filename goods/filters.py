from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline
from django.db.models.manager import BaseManager
from django.db.models import Q

from goods.models import Products


class ProductFilter:
	def __init__(self, query):
		self.query = query


class ProductFilterID:
	def __init__(self, query: str):
		self.query = query

	def search(self) -> BaseManager[Products]:
		return Products.objects.filter(id=int(self.query))


class ProductFilterTitle:
	def __init__(self, query: str):
		self.query = query

	def search(self) -> BaseManager[Products]:
		keywords = [word for word in self.query.split() if len(word) > 3]
		q_obj = Q()

		for token in keywords:
			q_obj |= Q(title__icontains=token)

		return Products.objects.filter(q_obj)


def query_search(query: str) -> BaseManager[Products] | None:
	if query.isdigit() and len(query) <= 5:
		return Products.objects.filter(id=int(query))
	vector = SearchVector("title", "description")
	query = SearchQuery(query)
	queryset = Products.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")
	queryset = queryset.annotate(headline=SearchHeadline(
		"title", query, start_sel="<span style='background-color: yellow;'>", stop_sel="</span>")).all()
	queryset = queryset.annotate(bodyline=SearchHeadline(
		"description", query, start_sel="<span style='background-color: yellow;'>", stop_sel="</span>")).all()

	return queryset
