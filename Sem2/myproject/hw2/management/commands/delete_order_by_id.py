from django.core.management.base import BaseCommand

from myproject.hw2.models import Order


class Command(BaseCommand):
    help = f'Удаление по id Заказа'

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help='id заказа')

    def handle(self, *args, **options):
        order_id = options.get('order_id')
        order = Order.objects.filter(pk=order_id).first()
        order.delete()
        self.stdout.write(f'Заказ с id {order_id} успешно удален.')