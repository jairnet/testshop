from django.contrib import admin
from apps.product.models import Product
# Register your models here.
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
	list_display = ('name','brand','category','vendor','price','taxe')
	list_filter = ('name','brand','category')