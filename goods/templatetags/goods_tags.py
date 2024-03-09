from django import template
from django.utils.http import urlencode

from goods.models import Categories
from utils.redis_utils import get_redis_connection

register = template.Library()


@register.simple_tag
def get_categories():
    """
    Django тег для получения всех категорий.

    Использование в шаблоне:
    {% get_categories as categories %}
    categories содержит все объекты категорий.

    """
    cache = get_redis_connection()
    data = cache.get("categories")
    if data is None:
        data = Categories.objects.all()
        cache.set("categories", data)
    return data


@register.simple_tag(takes_context=True)
def context_params(context, **kwargs):
    """
    Django тег для обновления параметров запроса с использованием контекста.

    Использование в шаблоне:
    {% context_params param1=value1 param2=value2 %}

    Функция принимает текущий контекст и обновляет параметры запроса значениями kwargs,
    затем возвращает строку с обновленными параметрами в формате URL-кодировки.

    """
    query = context["request"].GET.dict()
    query.update(kwargs)
    return urlencode(query)
