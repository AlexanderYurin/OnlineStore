from django.contrib import admin
from goods.models import Categories, Products


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
	list_display = ["id", "title"]
	prepopulated_fields = {
		"slug": ["title"]
	}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
	list_display = ["title", "quantity", "price", "discount", "id_category"]
	prepopulated_fields = {
		"slug": ["title"]
	}
	list_editable = ["quantity", "price", "discount"]
	list_filter = ["title", "id_category__title", "quantity"]
	search_fields = ["title"]
	fields = ["title", "slug", "id_category",
			  "description", "quantity", ("price", "discount")]
