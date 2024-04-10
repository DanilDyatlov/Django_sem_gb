from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import logging

from django.utils.timezone import now
from datetime import timedelta

from .forms import ProductForm
from .models import Customer, Order, Product


logger = logging.getLogger(__name__)


def index(request):
    logger.info(f'Посещение страницы {__name__}: index')
    return render(request, 'h4app/index.html')


def about(request):
    logger.info(f'Посещение страницы {__name__}: about')
    return render(request, 'h4app/about.html')

# Заказы
def orders(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    order = Order.objects.filter(customer=customer).order_by('-pk')
    context = {'customer': customer, 'orders': order}
    return render(request, 'h4app/orders.html', context)

# Статус заказа
def stats(request, customer_id, scope_in_days=365):
    scope_dict = {}
    if scope_in_days not in (7, 30, 365):
        scope_dict.setdefault(f'{scope_in_days}', [])
    else:
        scope_dict.update({'7': [], '30': [], '365': []})
    customer = get_object_or_404(Customer, pk=customer_id)
    context = {'customer': customer}
    for k, v in scope_dict.items():
        order = Order.objects.filter(customer=customer,
                                      time_stamp_on_create__gt=now() - timedelta(days=int(k)))
        products = set([p for o in order for p in o.products.all()])
        products = list(products)
        products.sort(key=lambda x: x.price, reverse=True)
        scope_dict[k].extend(products)
    context['scope_dict'] = scope_dict
    return render(request, 'h4app/stats.html', context)

# Создание продукта
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            product = Product(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                quantity=form.cleaned_data['quantity'],
                time_stamp_on_create=now(),
            )
            product.save()
            logger.info(f'{product} успешно добавлен в базу')
    else:
        form = ProductForm()
    context = {'form': form, 'title': 'Форма создания нового товара'}
    return render(request, 'h4app/create.html', context)

#Обновление
def update_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
    form = ProductForm(instance=product)
    context = {'product': product, 'form': form, 'title': 'Форма обновления данных товара'}
    return render(request, 'h4app/update.html', context)