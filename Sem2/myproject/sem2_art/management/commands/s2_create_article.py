from datetime import timedelta, datetime
from random import randint, choice

from django.core.management.base import BaseCommand

from myproject.sem2_art.models import Author, Article


class Command(BaseCommand):
    help = 'Создание статьи'

    def handle(self, *args, **options):
        author = choice(Author.objects.all())
        j = randint(700, 800)
        article = Article(
            title=f'Article_{j}_Title',
            content=f'Article_{j}_Content',
            time_stamp=datetime.now() - timedelta(days=(randint(0, 60)), ),
            author=author,
            category=f'Категория_{randint(1, 20)}',
        )
        article.save()
        self.stdout.write(f'{article}')