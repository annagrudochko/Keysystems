from django.shortcuts import render
from django.http.request import HttpRequest


# первая клиентская страница
def index_2(request: HttpRequest):
    context = {
    }
    return render(request, 'index_2.html', context)


def index_2_1(request: HttpRequest):
    context = {
    }
    return render(request, 'index_2_1.html', context)


def index_2_2(request: HttpRequest):
    context = {
    }
    return render(request, 'index_2_2.html', context)


def index_3_1(request: HttpRequest):
    context = {
    }
    return render(request, 'index_3_1.html', context)


def index_3_2(request: HttpRequest):
    context = {
    }
    return render(request, 'index_3_2.html', context)
