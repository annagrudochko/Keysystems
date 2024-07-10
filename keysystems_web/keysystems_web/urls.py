"""
URL configuration for keysystems_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import: from my_app import views
    2. Add a URL to urlpatterns: path('', views.home, name='home')
Class-based views
    1. Add an import: from other_app.views import Home
    2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from auth_app import views as main
from client_app import views as client

urlpatterns = [
    path('', main.index_2, name='index_2'),
    path('index_2', main.index_2, name='index_2'),
    path('index_2_1', client.index_2_1, name='index_2_1'),
    path('index_2_2', client.index_2_2, name='index_2_2'),
    path('index_3_1', client.index_3_1, name='index_3_1'),
    path('index_3_2', client.index_3_2, name='index_3_2'),
    path('index_4_1', client.index_4_1, name='index_4_1'),
    path('index_4_2', client.index_4_2, name='index_4_2'),
    path('admin/', admin.site.urls),
]
