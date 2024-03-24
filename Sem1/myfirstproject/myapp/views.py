from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    context = {
        'text': 'Добро пожаловать на мой первый сайт на Django. \
           Это главная страница на которой я написал эту информацию.'
    }
    return render(request, 'myapp/index.html', context=context)


def about(request):
    html = "<h1>Это страница обо мне</h1>"
    logger.info(f'Показана информация: {html}')
    return HttpResponse(html)