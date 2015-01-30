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

	#pass in date object, get the list of farmers with that product that are able to source it
	def getFarmers(self, theDate):
		derpmers = self.farmer_set.all()
		retFarmers = []
		for derp in derpmers:
			for farmdate in derp.avail_set.all():
				print farmdate.date
				if farmdate.date == theDate:
					retFarmers.append(derp)
		return retFarmers


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


class Avail(models.Model):
	farmer = models.ForeignKey(Farmer)
	date = models.DateField(auto_now=False)


class Order(models.Model):
	cost = models.IntegerField(default=0)
	time = models.DateTimeField(auto_now=True)
	#user = models.ForeignKey(User)

class Fulfillment(models.Model):
	order = models.ForeignKey(Order)
	time = models.DateTimeField(auto_now=True)

'''
api = pm.PostmatesAPI("f8aa101d-6bc5-400d-96a1-ac7ee4a38c28", "cus_KBZUGmEchkNykk")

pickup = pm.Location('Alice', 'Union Square, New York, NY 10011', '415-555-0000')
dropoff = pm.Location('Bob', '301 w 110th st, New York, NY 10026', '415-777-9999')

quote = pm.DeliveryQuote(api, pickup.address, dropoff.address)
print quote
'''
