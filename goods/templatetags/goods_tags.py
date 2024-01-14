from django import template
from django.utils.http import urlencode

from goods.models import Categories

register = template.Library()


@register.simple_tag()
def get_categories():
    return Categories.objects.all()


@register.simple_tag(takes_context=True)
def context_params(context, **kwargs):
    query = context["request"].GET.dict()
    query.update(kwargs)
    return urlencode(query)
