from django.shortcuts import render

# Create your views here.

import logging

# Настройка журнала
logger = logging.getLogger(__name__)

def home(request):
    logger.info('Страница "Главная" была открыта.')
    return render(request, 'home.html')

def about_me(request):
    logger.info('Страница "О себе" была открыта.')
    return render(request, 'about_me.html')
