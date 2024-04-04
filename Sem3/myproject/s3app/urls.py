from django.urls import path
from . import views

urlpatterns = [
    path('articles_by_author_id/<int:author_id>', views.articles_by_author_id, name='articles_by_author_id'),
    path('article_by_id/<int:article_id>', views.article_by_id, name='article_by_id'),
    path('article_stats_by_id/<int:article_id>', views.article_stats_by_id, name='article_stats_by_id'),
]