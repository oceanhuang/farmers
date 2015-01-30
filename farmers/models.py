from django.db import models
import libs.postmates as pm

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

	products = models.ManyToManyField(Product)

	#availabilities
	#locations

class Availability(models.Model):
	farmers = models.ForeignKey(Farmer)
	date = models.DateField(auto_now=False)

'''
api = pm.PostmatesAPI("f8aa101d-6bc5-400d-96a1-ac7ee4a38c28", "cus_KBZUGmEchkNykk")

pickup = pm.Location('Alice', 'Union Square, New York, NY 10011', '415-555-0000')
dropoff = pm.Location('Bob', '301 w 110th st, New York, NY 10026', '415-777-9999')

quote = pm.DeliveryQuote(api, pickup.address, dropoff.address)
print quote
'''