from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .forms import UserRegistrationForm, UserEditForm
from .mixins import UserRequiredMixin


class IndexView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, 'users/index.html', context={
            'users': users,
        })


class CreateUserView(View):
    def get(self, request, *args, **kwargs):
        form = UserRegistrationForm()
        return render(request, 'users/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            msg_text = _('User is successfully created')
            messages.success(request, msg_text) 
            return redirect('users_login')
        return render(request, 'users/create.html', {'form': user_form})


class EditUserView(UserRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('home_users')
    success_message = _('User successfully changed')

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        form = UserEditForm(instance=user)
        return render(request,
                      'users/update.html',
                      {'form': form,
                       'user_id': user_id})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            msg_text = _('User successfully changed')
            messages.success(request, msg_text)
            return redirect('index')

        return render(request,
                     'users/update.html',
                     {'form': form,
                      'user_id':user_id})


class DeleteUserView(UserRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        full_username = f'{user.first_name} {user.last_name}'
        return render(request,
                      'users/delete.html',
                      context={'user_id': user_id,
                      'full_username': full_username})


    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('id')
        user = User.objects.get(id=user_id)
        if user:
            user.delete()
            msg_text = _('User deleted successfully')
            messages.success(request, msg_text)
            return redirect('users_index')


class LoginUserView(View):
    def get(self, request, *args, **kwargs):
        form = AuthenticationForm
        return render(request, 'users/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, _('You are logged in'))
            return redirect('index')
        return render(request, 'users/login.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.info(request, _('You are logged out'))
    return redirect('index')
