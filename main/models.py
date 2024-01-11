from django.db import models


# Create your models here.
class Main(models.Model):
	pass


class About(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=500)


class Delivery(models.Model):
	pass


class Contacts(models.Model):
	pass
