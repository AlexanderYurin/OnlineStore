from django.urls import path
from main.views import main, about


app_name = "main"

urlpatterns = [
    path("", main, name="main"),
    path("about/", about, name="about")
]