from django.urls import path
from goods.views import product, ListView, catalog


app_name = "catalog"


urlpatterns = [
    path("", catalog, name="catalog"),
    path("product/", product, name="product")
]