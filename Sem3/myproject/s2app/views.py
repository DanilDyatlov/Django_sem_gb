import logging

from random import choice, randint

from django.shortcuts import render

logger = logging.getLogger(__name__)


def heads_and_tails(request):
    title = 'Орел или Решка'
    result = f'{choice(["Орел", "Решка", ])}'
    context = {
        'title': title,
        'result': str(result),
    }
    logger.info(f'{title}: {result}')
    return render(request, 's2app/game.html', context)


def roll_the_dice(request):
    title = 'Бросок кубика'
    result = f'{randint(1, 6)}'
    context = {
        'title': title,
        'result': str(result),
    }
    logger.info(f'{title}: {result}')
    return render(request, 's2app/game.html', context)


def random_number(request):
    title = 'Случайное число от 1 до 100'
    result = f'{randint(0, 100)}'
    context = {
        'title': title,
        'result': str(result),
    }
    logger.info(f'{title}: {result}')
    return render(request, 's2app/game.html', context)
