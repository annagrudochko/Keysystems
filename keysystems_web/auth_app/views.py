from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.contrib.auth import login, logout


from .forms import AuthBaseForm
from base_utils import log_error
from enums import RequestMethod


# распределяет пользователей
# def login_view(request: HttpRequest):
#     if request.user.is_authenticated:
#         return redirect('index_4_1')


# выход
def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        logout(request)
        return redirect('login')


# первая клиентская страница
def index_2(request: HttpRequest):
    log_error(request.method, wt=False)
    input_error = 0
    if request.method == RequestMethod.POST:
        form = AuthBaseForm(request.POST)
        if form.is_valid():
            return redirect('index_2_1')
        else:
            input_error = 1

    context = {'input_error': input_error}
    return render(request, 'index_2.html', context)
