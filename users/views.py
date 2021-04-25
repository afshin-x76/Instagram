from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import User

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, 'users/login.html', context=context)

    def post(self, request):
        username =request.POST['username']
        password = request.POST['password']
        print(request.POST['username'])
        user = authenticate(request, username=username, password=password)
        if user:
            print('in validation')
            login(request, user)
            return HttpResponse('Login Successfully')

        return HttpResponse('You are not authenticated')


class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        context = {
            'form': form,
        }
        return render(request, 'users/signup.html', context=context)

    def post(self, request):
        print(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password = request.POST['password2']
        birthday = request.POST['date_of_birth']
        form = UserRegisterForm(request.POST)
        # print(form)
        if form.is_valid():
            print('in validdddddddddddddddddddddddddddddddddddd')
            form.save()
            return HttpResponse('register successfully')
        return HttpResponse('Not Valid')

def logout_user(request):
    _from = request.META.get('HTTP_REFERER')
    logout(request)
    return redirect(_from)