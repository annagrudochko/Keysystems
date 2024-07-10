from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserKS


# проверка инн
class AuthBaseForm(forms.Form):
    inn = forms.IntegerField()


# форма регистрации
class RegistrationForm(forms.Form):
    inn = forms.IntegerField(min_value=1000000000, max_value=999999999999)
    email = forms.CharField()
    fio = forms.CharField()
    tel = forms.CharField()
    reg_progr = forms.CharField()

    # class Meta:
    #     model = UserKS
    #     fields = ('inn', 'email', 'full_name', 'phone')
