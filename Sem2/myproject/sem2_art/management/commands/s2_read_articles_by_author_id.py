from django.core.management.base import BaseCommand

from myproject.sem2_art.models import Article


class Command(BaseCommand):
    help = 'Выборка статей по id автора'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='ID автора')

    def handle(self, *args, **options):
        pk = options.get('pk')
        articles = Article.objects.filter(author__pk=pk)
        out = '\n'.join(a.content for a in articles)
        self.stdout.write(f'{out}')