from django.urls import path
from . import views

urlpatterns = [
    path('articles_by_author_firstname/<str:author_firstname>/',
         views.articles_by_author_firstname,
         name='articles_by_author_firstname'),
    path('articles_by_author_firstname/<str:author_firstname>/<int:max_results>',
         views.articles_by_author_firstname,
         name='articles_by_author_firstname'),
    path('articles_by_author_firstname/<str:author_firstname>/<int:max_results>/<str:filter_by>',
         views.articles_by_author_firstname,
         name='articles_by_author_firstname'),
    path('comments_by_author_firstname/<author_firstname>',
         views.comments_by_author_firstname,
         name='comments_by_author_firstname'),
    path('comments_by_article_title/<article_title>',
         views.comments_by_article_title,
         name='comments_by_article_title'),
]