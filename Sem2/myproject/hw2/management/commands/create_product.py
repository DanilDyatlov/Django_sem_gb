from decimal import Decimal

from django.utils.timezone import now
from django.core.management.base import BaseCommand

from myproject.hw2.models import Product


class Command(BaseCommand):
    help = f'Создание записи Товара'

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='Наименование товара')
        parser.add_argument('description', type=str, help='Описание товара')
        parser.add_argument('price', type=Decimal, help='Цена товара')
        parser.add_argument('quantity', type=int, help='Количество товара')

    def handle(self, *args, **options):
        title = options.get('title')
        description = options.get('description')
        price = options.get('price')
        quantity = options.get('quantity')
        product = Product(
            title=title,
            description=description,
            price=price,
            quantity=quantity,
            time_stamp_on_create=now(),
        )
        product.save()

        self.stdout.write(f'{product}')