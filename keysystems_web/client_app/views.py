from django.shortcuts import render, redirect
from django.http.request import HttpRequest

from .forms import AuthUserForm
from enums import RequestMethod


def index_2_2(request: HttpRequest):
    context = {}
    return render(request, 'index_2_2.html', context)


def index_3_1(request: HttpRequest):
    context = {
    }
    return render(request, 'index_3_1.html', context)


def index_3_2(request: HttpRequest):
    text = [
        {'title': 'Ускорение',
         'text': 'В последнее время пользователи Кейсистем заметили значительное увеличение скорости соединения. '
                 'Это стало возможным благодаря обновлению инфраструктуры и оптимизации сетевых маршрутов. '
                 'Теперь пользователи могут воспользоваться более быстрой и надежной связью, что особенно важно для '
                 'работы и учебы удаленно.',
         'day': '1',
         'month': 'Июля',
         'year': '2024',
         'author': 'Иван Иванов',
         'photo': '/media/news/example.jpg',
        },
        {'title': 'Расширение',
         'text': 'Кейсистем представил новые услуги для своих клиентов. Среди них – бесплатный Wi-Fi в общественных '
                 'местах, расширенный пакет данных для мобильных устройств и скидки на абонентскую плату для новых '
                 'подписчиков. Эти изменения направлены на улучшение качества жизни пользователей и '
                 'привлечение новых клиентов.',
         'day': '15',
         'month': 'Июля',
         'year': '2024',
         'author': 'Петр Петров',
         'photo': '/media/news/example.jpg',
         },
        {'title': 'Модернизация',
         'text': 'Текст: Для обеспечения стабильности и надежности связи Кейсистем проводит масштабное обновление '
                 'своего оборудования. Более 50% базовых станций уже были модернизированы, а остальные будут '
                 'обновлены к концу года. Это позволит улучшить покрытие и качество сигнала в регионе.',
         'day': '20',
         'month': 'Июля',
         'year': '2024',
         'author': 'Сергей Сергеев',
         'photo': '/media/news/example.jpg',
         },
        {'title': 'Экологическая инициатива',
         'text': 'Текст: Кейсистем запустил экологическую программу, направленную на снижение влияния своей '
                 'деятельности на окружающую среду. В рамках этой инициативы компания планирует установить солнечные '
                 'панели на крышах своих объектов и использовать возобновляемую энергию для питания серверов. '
                 'Это не только поможет сэкономить ресурсы, но и сделает работу компании более устойчивой к '
                 'изменяющимся условиям климата.',
         'day': '30',
         'month': 'Июля',
         'year': '2024',
         'author': 'Мария Марина',
         'photo': '/media/news/example.jpg',
         },
    ]
    context = {'news': text}
    return render(request, 'index_3_2.html', context)


def index_4_1(request: HttpRequest):
    context = {
    }
    return render(request, 'index_4_1.html', context)


def index_4_2(request: HttpRequest):
    context = {
    }
    return render(request, 'index_4_2.html', context)
