from typing import Any, Dict
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView

from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from products.models import Basket


class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "users/registration.html"
    success_url = reverse_lazy("users:login")
    # success_message = "Вы успешно зарегестрированы!"
    title = "Store - Регистрация"


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = "users/profile.html"
    # title = 'Store - Личный кабинет'

    def get_success_url(self):
        return reverse_lazy("users:profile", args=(self.object.id,))

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Store - Profile"
        context["baskets"] = Basket.objects.filter(user=self.object)
        return context
