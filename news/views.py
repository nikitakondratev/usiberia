from django.shortcuts import render
from django.views import generic
from .models import Article


def news(request):
    """
    Функция отображения для новостной страницы сайта.
    """

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request, 'news.html',
    )


class NewsView(generic.DetailView):
    model = Article
