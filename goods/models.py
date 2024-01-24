from django.db import models
from django.urls import reverse


# Create your models here.

class Categories(models.Model):
	title = models.CharField(max_length=100, unique=True, verbose_name="Название")
	slug = models.SlugField(verbose_name="URL", unique=True)

	class Meta:
		db_table = "Category"
		verbose_name = "Категорию"
		verbose_name_plural = "Категории"

	def __str__(self):
		return self.title


class Products(models.Model):
	slug = models.SlugField(unique=True, verbose_name="URL")
	title = models.CharField(max_length=100, verbose_name="Название")
	description = models.TextField(max_length=500, blank=True, null=True, verbose_name="Описание")
	image = models.ImageField(upload_to="products", blank=True, null=True, verbose_name="Изображение")
	quantity = models.PositiveIntegerField(default=0, verbose_name="Кол-во")
	price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name="Цена")
	discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name="Скидка")
	id_category = models.ForeignKey(Categories,
									on_delete=models.CASCADE,
									verbose_name="Категория",
									related_name="products")

	class Meta:
		db_table = "Product"
		verbose_name = "Товар"
		verbose_name_plural = "Товары"
		ordering = ["id"]

	def __str__(self) -> str:
		return self.title

	def get_absolute_url(self):
		return reverse("catalog:product", kwargs={"slug": self.slug})

	def display_id(self) -> str:
		return f"{self.id:05}"

	def sell_price(self):
		if self.discount:
			return round(self.price - self.discount * self.price / 100, 2)
		return self.price