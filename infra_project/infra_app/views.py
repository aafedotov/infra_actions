from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось! Новый релиз 2.0 УРА!')


def second_page(request):
    return HttpResponse('А это вторая страница! Новый релиз 2.0 УРА!')
