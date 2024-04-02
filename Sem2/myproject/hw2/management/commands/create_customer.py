from django.utils.timezone import now
from django.core.management.base import BaseCommand

from myproject.hw2.models import Customer


class Command(BaseCommand):
    help = f'Создание записи Клиента'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Имя пользователя')
        parser.add_argument('email', type=str, help='Email пользователя')
        parser.add_argument('phone_number', type=str, help='Номер телефона')

    def handle(self, *args, **options):
        username = options.get('username')
        email = options.get('email')
        phone_number = options.get('phone_number')
        customer = Customer(
            username=username,
            email=email,
            phone_number=phone_number,
            time_stamp_on_create=now(),
        )
        customer.save()
        self.stdout.write(f'{customer}')