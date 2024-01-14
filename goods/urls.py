from django.conf.urls.static import static
from django.urls import path

from app.settings import MEDIA_URL, MEDIA_ROOT
from goods.views import CategoryDetail, ProductDetail


app_name = "catalog"


urlpatterns = [
    path("search/", CategoryDetail.as_view(), name="search"),
    path("<slug:cat_slug>/", CategoryDetail.as_view(), name="catalog"),
    path("product/<slug:slug>/", ProductDetail.as_view(), name="product"),

]