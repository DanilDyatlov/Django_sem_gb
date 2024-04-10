from django.urls import path
from .views import index, about
from .views import orders_by_customer_id, stats_by_customer_id, create_product, update_product

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('customer/<int:customer_id>/orders/', orders_by_customer_id, name='orders_by_customer_id'),
    path('customer/<int:customer_id>/stats/', stats_by_customer_id, name='stats_by_customer_id'),
    path('customer/<int:customer_id>/stats/<int:scope_in_days>/', stats_by_customer_id, name='stats_by_customer_id'),
    path('product/new', create_product, name='create_product'),
    path('product/<int:product_id>/edit', update_product, name='update_product'),
]