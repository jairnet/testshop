from django.contrib import admin
from apps.client.models import Client

# Register your models here.
@admin.register(Client)
class AdminClient(admin.ModelAdmin):
	list_display = ('name','last_name','mail','address','phone','city','country')
	list_filter = ('name','last_name','city')