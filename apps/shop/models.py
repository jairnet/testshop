from django.db import models
from apps.client.models import Client
from apps.product.models import Product

# Create your models here.

class Order(models.Model):
	client = models.ForeignKey(Client)
	buy_date = models.DateField()
	delivery_date = models.DateField()
	shipping = models.DecimalField(max_digits=10, decimal_places=2)

	class Meta:
		ordering = ["id"]
		verbose_name_plural = "Orders"

	def __str__(self): # __unicode__ en Python 2
		return self.id

class Item(models.Model):
	order = models.ForeignKey(Order)
	product = models.ManyToManyField(Product)
	quantity = models.IntegerField(blank=False, null=False)
	
	class Meta:
		ordering = ["order_id"]
		verbose_name_plural = "Items"

	def __str__(self): # __unicode__ en Python 2
		return self.order_id
