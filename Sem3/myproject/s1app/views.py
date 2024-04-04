from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info(f'Посещение страницы {__name__}: index')
    return render(request, template_name='s3_app1_app/index.html')


def about(request):
    logger.info(f'Посещение страницы {__name__}: about')
    return render(request, template_name='s3_app1_app/about.html')