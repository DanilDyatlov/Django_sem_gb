# 📌 Настройте под свои нужды вывод информации о клиентах, товарах и заказах
# на страницах вывода информации об объекте и вывода списка объектов.
#
# >: python manage.py createsuperuser
# -> login at http://127.0.0.1:8000/admin/ with su
#
from django.contrib import admin
from .models import Customer, Product, Order


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone_number']
    ordering = ['username']
    search_fields = ['username']
    readonly_fields = ['time_stamp_on_create']
    fieldsets = [
        ('Данные клиента',
         {'classes': ['wide'], 'fields': ['username', 'email', 'phone_number', 'time_stamp_on_create']}),
    ]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'quantity', 'img']
    ordering = ['title']
    search_fields = ['title', 'description', 'price']
    readonly_fields = ['title', 'price', 'quantity', 'time_stamp_on_create']
    fieldsets = [
        ('Данные продукта', {'classes': ['wide'], 'fields': ['title']}),
        ('Маркетинг', {'classes': ['collapse'], 'fields': ['description', 'price', 'img']}),
        ('Склад', {'classes': ['collapse'], 'fields': ['quantity']}),
        (None, {'classes': ['wide'], 'fields': ['time_stamp_on_create']})
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total', 'time_stamp_on_create']
    ordering = ['customer']
    list_filter = ['customer', 'products']
    search_fields = ['products']
    readonly_fields = ['total', 'products', 'time_stamp_on_create']
    fieldsets = [
        ('Клиент', {'classes': ['wide'], 'fields': ['customer']}),
        ('Товары', {'classes': ['collapse'], 'fields': ['products', 'total']}),
        (None, {'classes': ['wide'], 'fields': ['time_stamp_on_create']})
    ]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)