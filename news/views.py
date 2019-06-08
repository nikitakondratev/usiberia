from django.shortcuts import render


def news(request):
    """
    Функция отображения для новостной страницы сайта.
    """

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request, 'news.html',
    )
