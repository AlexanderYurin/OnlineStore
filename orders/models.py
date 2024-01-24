from django.db import models

from goods.models import Products
from users.models import User


class OrderQuerySet(models.QuerySet):
	def total_price(self) -> int:
		return sum(product.product_price() for product in self)

	def total_quantity(self) -> int:
		if self:
			return sum(product.quantity for product in self)
		return 0


class Orders(models.Model):
	STATUS = (
		(1, "В обработке"),
		(2, "Принят"),
		(3, "В работе"),
	)

	user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, verbose_name="Пользователь",
							 related_name="orders", blank=True, null=True, default=None)
	date_created = models.DateTimeField(verbose_name="Дата создания заказа", auto_now_add=True)
	requires_delivery = models.BooleanField(default=False, verbose_name="Требуется доставка")
	address_delivery = models.TextField(blank=True, null=True, verbose_name="Адрес доставки")
	payment_on_get = models.BooleanField(default=False, verbose_name="Оплата при получение")
	is_paid = models.BooleanField(default=False, verbose_name="Оплачено")
	is_status = models.CharField(choices=STATUS, verbose_name="Статус заказа", default=STATUS[0])

	class Meta:
		db_table = "order"
		verbose_name = "Заказ"
		verbose_name_plural = "Заказы"

	def __str__(self):
		return f"Заказ: {self.id} | Покупатель: {self.user.first_name} {self.user.last_name} | Статус: {self.is_status}"


class OrderItems(models.Model):
	order = models.ForeignKey(Orders, on_delete=models.CASCADE, verbose_name="Заказ",
							  related_name="order_items", )
	product = models.ForeignKey(Products, on_delete=models.SET_DEFAULT, verbose_name="Товар",
								related_name="order_items", null=True, default=None)
	title = models.CharField(max_length=100, verbose_name="Название")
	quantity = models.PositiveIntegerField(default=0, verbose_name="Кол-во")
	price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="Цена")
	date_created = models.DateTimeField(verbose_name="Дата продажи товара", auto_now_add=True)

	objects = OrderQuerySet().as_manager()

	def product_price(self) -> float:
		return round(self.product.sell_price() * self.quantity, 2)

	class Meta:
		db_table = "order_item"
		verbose_name = "Проданный товар"
		verbose_name_plural = "Проданные товары"
		ordering = ["-date_created"]

	def __str__(self):
		return f"Товар: {self.title} | Кол-во: {self.quantity} | Цена: {self.price}"
