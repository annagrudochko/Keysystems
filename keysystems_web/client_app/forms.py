from django import forms


# проверка инн
class AuthUserForm(forms.Form):
    inn = forms.IntegerField()
    email = forms.EmailField()
