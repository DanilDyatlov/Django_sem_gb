from datetime import date, timedelta, datetime
from random import randint, choice

from django.core.management.base import BaseCommand

from myproject.s3app.models import Author, Article


class Command(BaseCommand):
    help = 'Генерация авторов и публикаций'

    def add_arguments(self, parser):
        parser.add_argument('authors', type=int, help='Количество авторов')
        parser.add_argument('articles', type=int, help='Количество публикаций у каждого автора')

    def handle(self, *args, **options):
        authors = options.get('authors')
        articles = options.get('articles')
        for i in range(1, authors + 1):
            author = Author(firstname=f'Firstname_{i}',
                            lastname=f'Lastname_{i}',
                            email=f'mail{i}@mail.ru',
                            biography=f'Biography_{i}',
                            birthday=f'{date.today() - timedelta(days=(365 * randint(16, 90) + randint(0, 365)))}',
                            )
            author.save()
            for j in range(1, articles + 1):
                article = Article(
                    title=f'Article_{j}_Title',
                    content=f'Article_{j}_Content',
                    time_stamp=datetime.now() - timedelta(days=(randint(0, 60)), ),
                    author=author,
                    category=f'Категория_{randint(1, 20)}',
                    is_published=choice([True, False])
                )
                article.save()