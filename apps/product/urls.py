from django.conf.urls import url
from apps.product.views import AllProdcuctsViews, ProductDetail, ProductCreate

urlpatterns = [
	url(r'^all/$', AllProdcuctsViews.as_view(), name='products'),
	url(r'^detail/(?P<pk>\d+)$', ProductDetail.as_view(), name='product_detail'),
	url(r'^create/$', ProductCreate.as_view(), name='product_create'),
]