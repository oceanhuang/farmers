from django.db import models

class Product(models.Model):
	category = models.CharField(max_length=200)
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	image = models.ImageField()
	weight = models.IntegerField(default=0)
	#handwaving
	price = models.IntegerField(default=0)
	amount = models.IntegerField(default=0)


class Farmer(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	phone = models.IntegerField(default=11111111111, max_length=10)

	products = models.ManyToManyField(Product)

	#availabilities
	#locations

class Availability(models.Model):
	farmers = models.ForeignKey(Farmer)
	date = models.DateField(auto_now=False)