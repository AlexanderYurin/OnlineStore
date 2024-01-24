from django.db import models

from goods.models import Products
from users.models import User


class CartQuerySet(models.QuerySet):
	def total_price(self) -> int:
		return sum(cart.product_price() for cart in self)

	def total_quantity(self) -> int:
		if self:
			return sum(cart.quantity for cart in self)
		return 0


class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь",
							 related_name="cart", blank=True, null=True)
	product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name="Товар",
								related_name="cart")
	quantity = models.PositiveIntegerField(default=0, verbose_name="Кол-во")
	session_key = models.CharField(max_length=32, blank=True, null=True)
	date_created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

	class Meta:
		db_table = "cart"
		verbose_name = "Корзина"
		verbose_name_plural = "Корзина"

	objects = CartQuerySet().as_manager()

	def product_price(self) -> float:
		return round(self.product.sell_price() * self.quantity, 2)

	def __str__(self):
		return f"Корзина: {self.user} | Товар: {self.product.title} | Количество: {self.quantity}"
