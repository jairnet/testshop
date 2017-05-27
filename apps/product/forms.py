from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [
				"name",
				"brand",
				"category", 
				"vendor", 
				"price", 
				"taxe", 
				"image", 
				"description"
		]
		# labels = {
		# 		"name": "Name",
		# 		"brand": "Brand",
		# 		"category": "Category", 
		# 		"vendor": "Vendor", 
		# 		"price": "Price", 
		# 		"taxe": "Taxe", 
		# 		"image": "Image", 
		# 		"description": "Description"
		# }

		# widgets = {
		# 		"name":forms.TextInput(attrs={'class':'form-control'}),
		# 		"brand":forms.TextInput(attrs={'class':'form-control'}),
		# 		"category", 
		# 		"vendor":forms.TextInput(attrs={'class':'form-control'}), 
		# 		"price":forms.TextInput(attrs={'class':'form-control'}), 
		# 		"taxe":forms.TextInput(attrs={'class':'form-control'}), 
		# 		"image", 
		# 		"description":forms.TextInput(attrs={'class':'form-control'}),

		# }
	
def clean(self, *args, **kwargs):
	cleaned_data = super(ProductForm, self).clean(*args, **kwargs)