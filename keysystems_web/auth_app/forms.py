from django import forms


# проверка инн
class AuthBaseForm(forms.Form):
    inn = forms.IntegerField()
