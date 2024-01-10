from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def main(request: HttpRequest) -> HttpResponse:
	context = {
		"title": "Test"
	}
	return render(request, "main/index.html", context)
