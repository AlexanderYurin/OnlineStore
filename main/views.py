from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from goods.models import Categories


# Create your views here.

class Index(ListView):
	model = Categories
	template_name = "main/index.html"

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data()
		context = {
			"title": "Магазин мебели для дома",
			"footer_text": "Test footer",
		}
		return context


# def main(request: HttpRequest) -> HttpResponse:
# 	context = {
# 		"title": "Test",
# 		"footer_text": "Test footer"
# 	}
# 	return render(request, "main/index.html", context)

def about(request: HttpRequest) -> HttpResponse:
	context = {
		"title": "О на",
		"description": "Текст о том какой классный этот интернет магазин.",
		"footer_text": "Test footer",
	}
	return render(request, "main/about.html", context)
