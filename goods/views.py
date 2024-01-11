from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.


def catalog(request: HttpRequest) -> HttpResponse:
	return render(request, template_name="goods/catalog.html")


def product(request: HttpRequest) -> HttpResponse:
	return render(request, template_name="goods/product.html")