import logging

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now


from .utils import validator

from .forms import AuthorForm, ArticleForm, CommentForm
from .models import Author, Article, Comment

logger = logging.getLogger(__name__)


def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if validator.is_value_present_in_db(email, Author, 'email'):
                return HttpResponse(f'Значение email: "{email}" уже присутствует в БД.')

            author = Author(firstname=form.cleaned_data['firstname'],
                            lastname=form.cleaned_data['lastname'],
                            email=form.cleaned_data['email'],
                            biography=form.cleaned_data['biography'],
                            birthday=form.cleaned_data['birthday'],
                            )
            author.save()
            logger.info(f'{author} успешно добавлен в базу')
    else:
        form = AuthorForm()
    context = {'form': form, 'title': 'Форма создания нового автора'}
    return render(request, 's2app/create.html', context)


def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            if validator.is_value_present_in_db(title, Article, 'title'):
                return HttpResponse(f'Значение title: "{title}" уже присутствует в БД.')

            article = Article(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                time_stamp=now(),
                author=form.cleaned_data['author'],
                category=form.cleaned_data['category'],
                views=form.cleaned_data['views'],
                is_published=form.cleaned_data['is_published'],
            )
            article.save()
            logger.info(f'{article} успешно добавлен в базу')
    else:
        form = ArticleForm()
    context = {'form': form, 'title': 'Форма создания новой статьи'}
    return render(request, 's2app/create.html', context)


def articles_by_author_id(request, author_id: int):
    author = Author.objects.filter(pk=author_id).first()
    articles = Article.objects.filter(author=author)
    context = {'author': author, 'articles': articles}
    return render(request, 's2app/articles_by_author_id.html', context)


def article_by_id(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = Comment.objects.filter(article=article).all().order_by('-time_stamp_modify')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            moment = now()
            comment = Comment(
                author=article.author,
                article=article,
                content=form.cleaned_data['content'],
                time_stamp_create=moment,
                time_stamp_modify=moment,
            )
            comment.save()
            logger.info(f'{comment} успешно добавлен в базу')
    else:
        form = CommentForm()
    if article.is_published:
        article.views += 1
        article.save()
    title = f'Статьи автора {article.author.full_name()}'
    context = {'article': article, 'comments': comments, 'form': form, 'title': title}
    return render(request, 's2app/article_by_id.html', context)


def article_stats_by_id(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {'article': article}
    return render(request, 's2app/article_stats_by_id.html', context)
