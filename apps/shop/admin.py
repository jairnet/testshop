from django.contrib import admin
from apps.shop.models import Order
from apps.client.models import Client
# Register your models here.
@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
	list_display = ('buy_date','delivery_date','shipping')
	list_filter = ('client_id','buy_date')