from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def main(request: HttpRequest) -> HttpResponse:
	return render(request, "main/index.html")
