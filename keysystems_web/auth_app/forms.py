from django import forms


# проверка инн
class AuthBaseForm(forms.Form):
    INN = forms.IntegerField()
