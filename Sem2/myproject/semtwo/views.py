import logging

from django.http import HttpResponse

from random import choice
from .models import Coin

logger = logging.getLogger(__name__)


def heads_and_tails(request):
    answer = f'{choice([Coin.H, Coin.T])}'
    coin = Coin(side=answer)
    coin.save()
    logger.info(f'Орел или Решка: {answer}')
    return HttpResponse(answer)


def stats(request, n: int):
    stats_dict = Coin.get_statistics(n)
    print(stats_dict)
    answer = (f'Статистика по последним {stats_dict["throws"]} броскам:<br>'
              f'Бросков с результатом {Coin.H}: {stats_dict["heads"]}, '
              f'процент выпадения: {round(100 / stats_dict["throws"] * stats_dict["heads"])}%<br>'
              f'Бросков с результатом {Coin.T}: {stats_dict["tails"]}, '
              f'процент выпадения: {round(100 / stats_dict["throws"] * stats_dict["tails"])}%<br>')
    return HttpResponse(answer)
