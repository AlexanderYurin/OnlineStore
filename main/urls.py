from django.urls import path
from main.views import Index, about


app_name = "main"

urlpatterns = [
    path("", Index.as_view(), name="main"),
    path("about/", about, name="about")
]