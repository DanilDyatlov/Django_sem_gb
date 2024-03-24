import logging
from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("Hello world!")


def eagle(request, count: int):
    game_list = ['орел', 'решка']
    result = []
    for i in range(count):
        response = random.choice(game_list)
        result.append(response)
    context = {
        'result': result
    }
    # coin = Coin(is_eagle=response)
    # coin.save()
    # logger.info(f'Значение: {coin}')
    return render(request, 'myapp/index.html', context=context)


def show_elements(request, n: int):
    pass


def cube(request):
    cube_value = random.randint(1, 6)
    logger.info(f'Кубик выпал стороной: {cube_value}')
    return HttpResponse(cube_value)


def random_number(request):
    number = random.randint(0, 100)
    logger.info(f'Случайное число: {number}')
    return HttpResponse(number)