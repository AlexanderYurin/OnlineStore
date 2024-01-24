from django.contrib import admin

from carts.admin import CartTabular
from orders.admin import OrderTabular
from users.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ["first_name", "last_name", "email"]
	list_filter = ["first_name", "last_name", "email"]

	inlines = [CartTabular, OrderTabular]