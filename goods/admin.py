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
	list_display = ["title", "quantity", "price", "id_category"]
	prepopulated_fields = {
		"slug": ["title"]
	}
