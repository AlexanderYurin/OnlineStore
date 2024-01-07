from django.db import models


# Create your models here.

class Category(models.Model):
	title = models.CharField()

	def __str__(self):
		return self.title


class Good(models.Model):
	slug = models.SlugField()
	title = models.CharField()
	description = models.CharField()
	image = models.ImageField()
	quantity = models.IntegerField(default=0)
	price = models.IntegerField()
	discount = models.IntegerField()
	sale = models.IntegerField()
	id_category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return self.title



