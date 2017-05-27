from django.db import models

# Create your models here.

class Client(models.Model):
	name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	mail = models.EmailField()
	address = models.CharField(max_length=50)
	phone = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	country = models.CharField(max_length=50)


	class Meta:
		ordering = ["name"]
		verbose_name_plural = "Clients"

	def __str__(self): # __unicode__ en Python 2
		return self.name

class Card(models.Model):
	TYPE_CARD_CHOICES = ( 
    ('MC', 'MasterCard'), 
    ('VS', 'Visa'),
    ('DN', 'Dinner'), 
    ('AE', 'American Express'),
	)
	name = models.CharField(max_length=50)
	number_card = models.IntegerField(blank=False, null=False)
	type_card = models.CharField(max_length=1,choices=TYPE_CARD_CHOICES) 
	security_number = models.IntegerField(blank=False, null=False)
	exp_date = models.CharField(max_length=50)
	client = models.ForeignKey(Client)

	class Meta:
		ordering = ["client"]
		verbose_name_plural = "Cards"

	def __str__(self): # __unicode__ en Python 2
		return self.client_id	