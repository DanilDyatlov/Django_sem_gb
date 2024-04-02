from django.core.management.base import BaseCommand

from myproject.hw2.models import Order


class Command(BaseCommand):
    help = f'Чтение по id Заказа'

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help='id заказа')

    def handle(self, *args, **options):
        order_id = options.get('order_id')
        order = Order.objects.filter(pk=order_id).first()
        self.stdout.write(f'{"-"*44} Заказ {order.pk} {"-"*44}')
        self.stdout.write(f'{order}')
        self.stdout.write(f'{"-"*40} Товары в заказе {"-"*40}')
        for product in order.products.all():
            print(product)
        self.stdout.write(f'{"-"*33} Общая сумма заказа: {order.total} {"-"*33}')