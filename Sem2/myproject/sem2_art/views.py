# Задание №7.
# 📌 Создайте функции для работы с базой данных:
#   ○ Поиск всех статей автора по его имени
#   ○ Поиск всех комментариев автора по его имени
#   ○ Поиск всех комментариев по названию статьи
# 📌 Каждая из трёх функций должна иметь возможность сортировки и ограничение выборки по количеству.

from django.http import HttpResponse
from .models import Article, Author, Comment


def articles_by_author_firstname(
        request,
        author_firstname: str,
        max_results: int = 0,
        filter_by='pk',
):
    author = Author.objects.filter(firstname=author_firstname).first()
    articles = Article.objects.order_by(filter_by).filter(author=author)
    result_list = [f'id:{a.pk} | title:{a.title} | content:{a.content}' for a in articles]
    max_results = max_results if max_results == 0 or len(result_list) >= max_results else len(result_list)
    result_list = result_list if max_results == 0 else result_list[:max_results]
    out = '<br>'.join(result_list)
    return HttpResponse(f'Articles of author with firstname "{author_firstname}":<br>{out}')


def comments_by_author_firstname(request, author_firstname):
    author = Author.objects.filter(firstname=author_firstname).first()
    comments = Comment.objects.filter(author=author)
    out = '<br>'.join(f'id:{c.pk} | content:{c.content}' for c in comments)
    return HttpResponse(f'Comments of author with firstname "{author_firstname}":<br>{out}')


def comments_by_article_title(request, article_title):
    articles = Article.objects.filter(title=article_title).all()
    out = ''
    for article in articles:
        comments = Comment.objects.filter(article=article)
        out += '<br>'.join(f'id:{c.pk} | article:{c.article.title} | content:{c.content}' for c in comments)
        out += '<br>'
    return HttpResponse(f'Comments for article with title "{article_title}":<br>{out}')
