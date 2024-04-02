from django.db import models
from django.db.models import query


# Задание №1.
# 📌 Создайте модель для запоминания бросков монеты: орёл или решка.
# 📌 Также запоминайте время броска


class Coin(models.Model):
    H = 'Орёл'  # heads
    T = 'Решка'  # tails
    side = models.CharField(choices=((H, 'Орёл'), (T, 'Решка')), max_length=5)
    throw_time = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f'{self.pk}, {self.side}'

    @staticmethod
    def get_statistics(n: int) -> dict:
        result = {}
        # Запросим броски с сортировкой в обратном порядке по дате
        coins_query = Coin.objects.order_by('-throw_time')
        # Если запрос статистики больше количества записей в БД -> обрежем запрос
        size_of_slice = int(n) if len(coins_query) >= int(n) else len(coins_query)
        coins = coins_query[:size_of_slice]
        # Запишем в результат общее количество бросков, кол-во орлов и решек
        result['throws'] = len(coins)
        result['heads'] = len({c.id: c.side for c in coins if c.side == Coin.H})
        result['tails'] = result['throws'] - result['heads']
        return result
