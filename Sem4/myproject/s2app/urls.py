from django.urls import path

from .views import create_author, create_article, articles_by_author_id, article_by_id, article_stats_by_id

urlpatterns = [
    path('author/new', create_author, name='create_author'),
    path('article/new', create_article, name='create_article'),
    path('articles_by_author_id/<int:author_id>', articles_by_author_id, name='articles_by_author_id'),
    path('article_by_id/<int:article_id>', article_by_id, name='article_by_id'),
    path('article_stats_by_id/<int:article_id>', article_stats_by_id, name='article_stats_by_id'),
]