from django import template

from goods.models import Categories


register = template.Library()


@register.simple_tag()
def get_categories():
    return Categories.objects.all()