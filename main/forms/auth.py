from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordChangeForm

class UserLoginForm(forms.Form):
    username = forms.CharField()
    username.widget.attrs['class'] = 'form-control'
    username.widget.attrs['placeholder'] = 'Usuário'
    password = forms.CharField(widget=forms.PasswordInput)
    password.widget.attrs['class'] = 'form-control'
    password.widget.attrs['placeholder'] = 'Senha'

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Verifique seu usuário e senha.')
            if not user.is_active:
                raise forms.ValidationError(
                    'Esta conta foi desativada, por favor contate um administrador.')
        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordChangeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'