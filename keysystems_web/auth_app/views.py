from django.shortcuts import render, redirect
from django.http.request import HttpRequest

from .forms import AuthBaseForm
from enums import RequestMethod


# первая клиентская страница
def index_2(request: HttpRequest):
    if request.method == RequestMethod.POST:
        form = AuthBaseForm(request.POST)
        if form.is_valid():
            redirect('index_2_1')

    context = {}
    return render(request, 'index_2.html', context)