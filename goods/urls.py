from django.conf.urls.static import static
from django.urls import path

from app.settings import MEDIA_URL, MEDIA_ROOT
from goods.views import product, CatalogList, catalog


app_name = "catalog"


urlpatterns = [
    path("", CatalogList.as_view(), name="catalog"),
    path("product/", product, name="product")
]