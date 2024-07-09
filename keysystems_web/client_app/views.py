from django.shortcuts import render, redirect
from django.http.request import HttpRequest

from .forms import AuthUserForm
from enums import RequestMethod


def index_2_1(request: HttpRequest):
    if request.method == RequestMethod.POST:
        form = AuthUserForm(request.POST)
        if form.is_valid():
            redirect('index_2_1')

    context = {}
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
