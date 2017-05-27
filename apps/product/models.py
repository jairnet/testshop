from django.db import models


# Create your models here.
class Product(models.Model):

	CATEGORY_CHOICES = ( 
    ('EC', 'Electronic'), 
    ('HM', 'Home'), 
    ('BK', 'Book'), 
    ('Cl', 'Clohing'), 
    ('TY', 'Toys'), 
	)

	name = models.CharField(max_length=50)
	brand = models.CharField(max_length=50)
	category = models.CharField(max_length=50,choices=CATEGORY_CHOICES)
	vendor = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	taxe = models.DecimalField(max_digits=10, decimal_places=2)
	image = models.ImageField(upload_to='portadas')
	description = models.TextField()
	 
	class Meta:
		ordering = ["name"]
		verbose_name_plural = "Products"

	def __str__(self): # __unicode__ en Python 2
		return self.name

