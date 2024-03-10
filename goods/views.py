from typing import Dict

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import QuerySet
from django.shortcuts import get_list_or_404
from django.views.generic import DetailView

from goods.models import Products
from goods.filters import query_search


class CategoryDetail(DetailView):
	"""
    Класс-представление для отображения списка продуктов в выбранной категории.
	Этот класс использует Django DetailView для отображения списка продуктов.
	в выбранной категории. Он также поддерживает поиск, фильтрацию по скидке и сортировку.
    """

	model = Products
	template_name = "goods/catalog.html"
	context_object_name = "products"
	slug_url_kwarg = "cat_slug"
	paginate_by = 3

	def get_object(self, queryset=None) -> QuerySet[Products]:
		"""
        Метод для получения объекта (списка продуктов) на основе параметров запроса.
        Метод учитывает параметры запроса, такие как категория, поиск, скидка и сортировка.
        """
		query = self.request.GET.get("q")
		slug = self.kwargs.get(self.slug_url_kwarg)

		if slug == "all":
			queryset = self.get_queryset()
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

		return queryset

	def get_context_data(self, **kwargs) -> Dict:
		"""
        Метод для получения контекстных данных для передачи в шаблон.
        """
		context = super().get_context_data()

		context["category_slug"] = self.kwargs.get(self.slug_url_kwarg)

		page = self.request.GET.get('page', 1)
		paginator = Paginator(context["products"], self.paginate_by)

		context["products"] = paginator.page(page)

		return context


class ProductDetail(DetailView):
	"""
    Класс-представление для отображения деталей конкретного продукта.

    Атрибуты:
        model: Класс модели для извлечения данных.
        template_name: Имя шаблона для отображения страницы.
        context_object_name: Имя переменной контекста для передачи в шаблон.

    Примечание:
        Этот класс использует Django DetailView для отображения деталей конкретного продукта.
    """

	model = Products
	template_name = "goods/product.html"
	context_object_name = "product"
