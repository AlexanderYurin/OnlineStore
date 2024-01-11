from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def main(request: HttpRequest) -> HttpResponse:
	context = {
		"title": "Test",
		"footer_text": "Test footer"
	}
	return render(request, "main/index.html", context)

def about(request: HttpRequest) -> HttpResponse:
	context = {
		"title": "О на",
		"description": "Текст о том какой классный этот интернет магазин.",
		"footer_text": "Test footer",
	}
	return render(request, "main/about.html", context)

