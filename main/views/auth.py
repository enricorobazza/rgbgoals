from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages


from main.forms.auth import UserLoginForm, UserPasswordChangeForm

class AuthView():
    def login(request):
        next_url = request.GET.get('next')
        if(request.user.is_authenticated):
            return redirect(next_url or '/')

        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect(next_url or '/')

        return render(request, 'auth/login.html', {'form': form})

    def logout(request):
        auth_logout(request)
        return redirect('/')

    def change_password(request):
        if request.method == 'POST':
            form = UserPasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user) 
                return redirect('index')
            else:
                return render(request, 'auth/change_password.html', {
                    'form': form
                })
        else:
            form = UserPasswordChangeForm(request.user)
        return render(request, 'auth/change_password.html', {
            'form': form
        })
