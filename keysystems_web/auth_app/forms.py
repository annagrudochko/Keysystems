from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserKS


# проверка инн
class AuthBaseForm(forms.Form):
    INN = forms.IntegerField()
    # class Meta:
    #     model = UserKS
    #     fields = ('inn')
