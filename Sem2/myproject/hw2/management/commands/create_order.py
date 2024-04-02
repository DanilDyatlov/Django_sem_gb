from django.utils.timezone import now
from django.core.management.base import BaseCommand

from myproject.hw2.models import Product, Customer, Order



class Command(BaseCommand):
    help = f'Создание Заказа по id Клиента и id Товара'

    def add_arguments(self, parser):
        parser.add_argument('customer_id', type=int, help='id клиента')
        parser.add_argument('product_id', type=int, help='id товара')

    def handle(self, *args, **options):
        customer_id = options.get('customer_id')
        product_id = options.get('product_id')
        order = Order(
            customer=Customer.objects.filter(pk=customer_id).first(),
            total=0,
            time_stamp_on_create=now(),
        )
        order.save()
        product_to_order = Product.objects.filter(pk=product_id).first()
        order.products.add(product_to_order)
        order.total = product_to_order.price
        order.save()
        self.stdout.write(f'{order}')