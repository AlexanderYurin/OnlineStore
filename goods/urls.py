from django.conf.urls.static import static
from django.urls import path

from app.settings import MEDIA_URL, MEDIA_ROOT
from goods.views import CatalogList, ProductDetail


app_name = "catalog"


urlpatterns = [
    path("", CatalogList.as_view(), name="catalog"),
    path("product/<slug:slug>/", ProductDetail.as_view(), name="product")
]