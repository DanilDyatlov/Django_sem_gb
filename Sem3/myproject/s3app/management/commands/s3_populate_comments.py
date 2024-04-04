from datetime import timedelta
from random import randint

from django.utils.timezone import now

from django.core.management.base import BaseCommand

from myproject.s3app.models import Article, Comment


class Command(BaseCommand):
    help = 'Генерация комментариев от 0 до 10 к каждой статье'

    def handle(self, *args, **options):
        articles = Article.objects.all()
        for article in articles:
            comments_qty = randint(0, 10)
            for i, _ in enumerate(range(comments_qty), 1):
                comment = Comment(author=article.author,
                                  article=article,
                                  content=f'Comment_{i}_Content',
                                  time_stamp_create=now() - timedelta(days=(randint(20, 60))),
                                  time_stamp_modify=now() - timedelta(days=(randint(0, 20))),
                                  )
                comment.save()
                self.stdout.write(f'{comment}')