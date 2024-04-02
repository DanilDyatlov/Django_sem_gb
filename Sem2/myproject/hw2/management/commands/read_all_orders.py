from django.core.management.base import BaseCommand

from myproject.hw2.models import Order


class Command(BaseCommand):
    help = f'Чтение по id Заказа'

    def handle(self, *args, **options):

        for order in Order.objects.all():
            self.stdout.write(f'{"-" * 44} Заказ {order.pk} {"-" * 44}')
            self.stdout.write(f'{order}')
            self.stdout.write(f'{"-" * 40} Товары в заказе {"-" * 40}')
            for product in order.products.all():
                print(product)
            self.stdout.write(f'{"-" * 33} Общая сумма заказа: {order.total} {"-" * 33}')