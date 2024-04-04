"""
Создайте шаблон для вывода всех заказов клиента и списком товаров внутри каждого заказа.
Создайте шаблон, который выводит список заказанных клиентом товаров из всех его заказов
с сортировкой по времени:
за последние 7 дней (неделю)
за последние 30 дней (месяц)
за последние 365 дней (год)
*Товары в списке не должны повторятся."""

from django.shortcuts import render, get_object_or_404
import logging

from django.utils.timezone import now
from datetime import timedelta

from .models import Order, Customer, Product

logger = logging.getLogger(__name__)


def index(request):
    logger.info(f'Посещение страницы {__name__}: index')
    return render(request, 'h3app/index.html')


def about(request):
    logger.info(f'Посещение страницы {__name__}: about')
    return render(request, 'h3app/about.html')


"""
Клиенты и заказы
"""


def orders(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    orders = Order.objects.filter(customer=customer).all()
    context = {'customer': customer, 'orders': orders}
    return render(request, 'h3app/orders.html', context)


"""
Статус заказа
Сортировка по дням
"""


def stats(request, customer_id, scope_in_days=365):
    scope_dict = {}
    if scope_in_days not in (7, 30, 365):
        scope_dict.setdefault(f'{scope_in_days}', [])
    else:
        scope_dict.update({'7': [], '30': [], '365': []})
    customer = get_object_or_404(Customer, pk=customer_id)
    context = {'customer': customer}
    for k, v in scope_dict.items():
        orders = Order.objects.filter(customer=customer,
                                      time_stamp_on_create__gt=now() - timedelta(days=int(k)))
        products = set([p for o in orders for p in o.products.all()])
        products = list(products)
        products.sort(key=lambda x: x.price, reverse=True)
        scope_dict[k].extend(products)
    context['scope_dict'] = scope_dict
    return render(request, 'h3app/stats.html', context)
