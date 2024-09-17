"""Импорт функции."""
from django.shortcuts import render


def about(request):
    """Рендеринг страницы о проекте."""
    return render(request, 'pages/about.html')


def rules(request):
    """Рендеринг страницы с правилами."""
    return render(request, 'pages/rules.html')
