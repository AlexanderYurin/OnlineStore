from django.contrib import admin

from carts.models import Cart


# Register your models here.
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
	list_display = ["get_user", "get_product_title", "quantity", "date_created"]
	list_filter = ["user", "product__title", "date_created"]

	def get_user(self, obj):
		if obj.user:
			return obj.user.username
		return "Анонимный пользователь"

	def get_product_title(self, obj):
		return obj.product.title


class CartTabular(admin.TabularInline):
	model = Cart
	fields = ["product", "quantity", "date_created"]
	search_fields = ["product__title", "quantity", "date_created"]
	readonly_fields = ["date_created"]
	extra = 1
