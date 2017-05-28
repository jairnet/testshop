from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Product
from .forms import ProductForm
# Create your views here.

class AllProdcuctsViews(ListView):
	model = Product
	template_name = "product/products_list.html"

class ProductDetail(DetailView):
	model = Product
	template_name = "product/product_detail.html"

class ProductCreate(CreateView):
	model = Product
	form_class = ProductForm
	temaplete_name = "product/product_form.html"
	success_url=reverse_lazy("product_detail")