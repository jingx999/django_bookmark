from django.shortcuts import render

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    # 登录成功之后的重定向地址
    def get_success_url(self):
        return reverse_lazy('bookmarks:bookmark_list')

class CustomLogoutView(LogoutView):
    # 登出之后重定向到登录界面
    next_page = reverse_lazy('accounts:login')

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

