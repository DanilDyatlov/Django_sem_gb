# Создайте шаблон для вывода всех статей автора в виде списка заголовков.
#   ○ Если статья опубликована, заголовок должен быть ссылкой на статью.
#   ○ Если не опубликована, без ссылки.
# Создай шаблон для вывода подробной информации о статье.
# 📌 Внесите изменения в views.py - создайте представление и в urls.py - добавьте маршрут.
# 📌 *Увеличивайте счётчик просмотра статьи на единицу при каждом просмотре.
# Измените шаблон для вывода заголовка и текста статьи, а также всех комментариев
# к статье с указанием текста комментария, автора комментария и даты обновления
# комментария в хронологическом порядке.
# 📌 Если комментарий изменялся, дополнительно напишите “изменено”.

from django.shortcuts import render, get_object_or_404

from .models import Author, Article, Comment


def articles_by_author_id(request, author_id: int):
    author = Author.objects.filter(pk=author_id).first()
    articles = Article.objects.filter(author=author)
    context = {'author': author, 'articles': articles}
    return render(request, 's3app/articles_by_author_id.html', context)


def article_by_id(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = Comment.objects.filter(article=article).all().order_by('-time_stamp_modify')
    context = {'article': article, 'comments': comments}
    if article.is_published:
        article.views += 1
        article.save()
    return render(request, 's3app/article_by_id.html', context)


def article_stats_by_id(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {'article': article}
    return render(request, 's3app/article_stats_by_id.html', context)
