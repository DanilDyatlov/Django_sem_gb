from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('customer/<int:customer_id>/orders/', views.orders_by_customer_id, name='orders'),
    path('customer/<int:customer_id>/stats/', views.stats_by_customer_id, name='stats'),
    path('customer/<int:customer_id>/stats/<int:scope_in_days>/', views.stats_by_customer_id, name='stats'),
]