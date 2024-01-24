from django.contrib import admin
from orders.models import Orders, OrderItems


class OrderItemTabular(admin.TabularInline):
	model = OrderItems
	fields = ["title", "quantity", "price", "date_created"]
	search_fields = ["title"]
	readonly_fields = ["date_created"]
	extra = 0


class OrderTabular(admin.TabularInline):
	model = Orders
	fields = ["requires_delivery", "payment_on_get", "is_paid", "is_status", "date_created"]
	search_fields = ["requires_delivery", "payment_on_get", "is_paid", "is_status", "date_created"]
	readonly_fields = ["date_created"]
	extra = 0


@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
	list_display = ["id", "user", "requires_delivery", "payment_on_get", "is_paid", "is_status", "date_created"]
	list_filter = ["user", "date_created", "is_status", "is_paid"]
	search_fields = ["user"]
	ordering = ["-date_created"]
	inlines = [OrderItemTabular]


@admin.register(OrderItems)
class OrderItemAdmin(admin.ModelAdmin):
	list_display = ["title", "quantity", "price", "date_created"]
	list_filter = ["title", "order__id", "quantity", "date_created"]
	search_fields = ["order", "title"]
	ordering = ["-date_created"]
