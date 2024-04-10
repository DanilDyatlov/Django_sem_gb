from decimal import Decimal
from datetime import timedelta
from random import randint, uniform, choice

from django.utils.timezone import now
from django.core.management.base import BaseCommand

from myproject.h4app.models import Customer, Product, Order


class DBDataError(Exception):
    pass


class Command(BaseCommand):
    help = (f'Генерация записей Клиента, Товара и Заказа с последующим сохранением в БД. '
            f'Примеры использования: '
            f'"python manage.py populate_db 10 20 5", '
            f'"python manage.py populate_db 0 0 5". '
            )

    def add_arguments(self, parser):
        parser.add_argument('customers_qty', type=int, help='Количество клиентов')
        parser.add_argument('products_qty', type=int, help='Количество товаров')
        parser.add_argument('orders_qty', type=int, help='Количество заказов')

    def handle(self, *args, **options):
        customers_qty = options.get('customers_qty')
        products_qty = options.get('products_qty')
        orders_qty = options.get('orders_qty')

        # Определим стартовые номера счетчиков во избежание повторов
        customers_start_counter = len(Customer.objects.all())
        products_start_counter = len(Product.objects.all())
        orders_start_counter = len(Order.objects.all())

        # Создание Клиентов
        for i in range(customers_start_counter + 1, customers_start_counter + customers_qty + 1):
            customer = Customer(
                username=f'Customer_{i}',
                email=f'mail_{i}@mail.ml',
                phone_number=f"+7{''.join([str(randint(0, 9)) for _ in range(10)])}",
                time_stamp_on_create=now() - timedelta(
                    days=randint(1, 200),
                    hours=randint(1, 23),
                    minutes=randint(0, 59)
                ),
            )
            customer.save()

        # Создание Товаров
        for i in range(products_start_counter + 1, products_start_counter + products_qty + 1):
            product = Product(
                title=f'Product_{i}_Title',
                description=f'Product_{i}_Description',
                price=round(uniform(1, 10_000), 2),
                quantity=randint(1, 100),
                time_stamp_on_create=now() - timedelta(
                    days=randint(1, 200),
                    hours=randint(1, 23),
                    minutes=randint(0, 59),
                ),
            )
            product.save()

        # Создание Заказов
        # Проверка на существующие записи Клиентов и Товаров
        customers = Customer.objects.all()
        if len(customers) == 0:
            raise DBDataError('В БД отсутствуют Клиенты')
        products = Product.objects.all()
        if len(products) == 0:
            raise DBDataError('В БД отсутствуют Товары')

        for i in range(orders_start_counter + 1, orders_start_counter + orders_qty + 1):
            order = Order(
                customer=choice(customers),
                total=0,
                time_stamp_on_create=now() - timedelta(
                    days=randint(1, 200),
                    hours=randint(1, 23),
                    minutes=randint(0, 59),
                ),
            )
            order.save()
            # Наполнение заказа товарами и расчет общей стоимости
            products_to_order = [choice(products) for _ in range(randint(1, 5))]
            order.products.set(products_to_order)
            order.total = sum([Decimal(i.price) for i in order.products.all()])
            order.save()

        self.stdout.write(
            f'БД успешно заполнена клиентами: {customers_qty}, товарами: {products_qty}, заказами: {orders_qty}')