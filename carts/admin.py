from django.contrib import admin

from carts.models import Cart


# Register your models here.
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
	pass