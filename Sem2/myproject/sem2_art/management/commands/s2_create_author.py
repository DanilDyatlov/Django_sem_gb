from datetime import date, timedelta
from random import randint

from django.core.management.base import BaseCommand

from myproject.sem2_art.models import Author


class Command(BaseCommand):
    help = 'Создание автора'

    def handle(self, *args, **options):
        i = randint(700, 800)
        author = Author(firstname=f'Firstname_{i}',
                        lastname=f'Lastname_{i}',
                        email=f'mail{i}@mail.ru',
                        biography=f'Biography_{i}',
                        birthday=f'{date.today() - timedelta(days=(365 * randint(16, 90) + randint(0, 365)))}',
                        )
        author.save()
        self.stdout.write(f'{author}')