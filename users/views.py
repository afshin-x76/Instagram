from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import User
from django.views.generic import ListView, DetailView

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
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print('in validdddddddddddddddddddddddddddddddddddd')
            form.save()
            return HttpResponse('register successfully')
        return HttpResponse('Not Valid')

def logout_user(request):
    _from = request.META.get('HTTP_REFERER')
    logout(request)
    return redirect(_from)


class UsersListView(ListView):
    model = User
    template_name = 'users/users-list.html'
    paginate_by = 10
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = User
    template_name = 'users/user-detail.html'
    context_object_name = 'user'


class FollowView(View):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        follower = User.objects.get(pk=request.user.pk)
        follower.follow.add(user)
        request.user.save()
        print(request.user.follow)
        follower.follow.add(user)
        follower.save()
        return redirect(request.META['HTTP_REFERER'])