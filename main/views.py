from django.shortcuts import render


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request, 'index.html',
    )


def about_view(request):
    return render(
        request, 'about.html',
    )


def contacts_view(request):
    return render(
        request, 'contacts.html',
    )


def account_view(request):
    return render(
        request, 'account.html',
    )
