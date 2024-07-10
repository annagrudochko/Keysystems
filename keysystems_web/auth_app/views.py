from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.contrib.auth import login, logout
from django.urls import reverse

from .forms import AuthBaseForm
from .models import UserKS
from base_utils import log_error
from enums import RequestMethod, UserRole


# Определяет начальную страницу пользователя
def start_page_redirect(request: HttpRequest):
    if request.user.is_authenticated and request.user.role == UserRole.CLIENT:
        return redirect('index_4_1')

    elif request.user.is_authenticated and request.user.role == UserRole.STAFF:
        return redirect('index_4_1')

    else:
        return redirect('index_2')


# выход
def logout_view(request):
    logout(request)
    return redirect('index_2')


# первая клиентская страница. Просит инн
def index_2(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('')

    log_error(request.method, wt=False)
    input_error = 0
    if request.method == RequestMethod.POST:
        return redirect('index_2_1')
        # log_error(request.POST, wt=False)
        # form = AuthBaseForm(request.POST)
        # if form.is_valid():
        #     user_inn = form.cleaned_data["INN"]
        #     users_inn = UserKS.objects.filter(inn=user_inn).all()
        #     log_error(f'{users_inn}', wt=False)
        #     log_error(f'len(users_inn): {len(users_inn)}', wt=False)
        #     if len(users_inn) == 0:
        #         return redirect('index_3_1')
        #
        #     elif len(users_inn) > 1:
        #         return redirect(reverse('index_2_1') + f'?inn={users_inn}')
        #
        #     else:
        #         return redirect('index_2_2')
        # else:
        #     input_error = 1

    context = {'input_error': input_error}
    return render(request, 'index_2.html', context)


def index_2_1(request: HttpRequest):
    # if request.method == RequestMethod.POST:
    #     form = AuthUserForm(request.POST)
    #     if form.is_valid():
    #         redirect('index_2_1')
    if request.method == RequestMethod.GET:
        inn = request.GET['inn']
        log_error(inn, wt=False)

    context = {'INN': inn}
    return render(request, 'index_2_1.html', context)