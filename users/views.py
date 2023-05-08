from typing import Any, Dict
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from products.models import Basket


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("index"))
    else:
        form = UserLoginForm
    context = {"form": form}
    return render(request, "users/login.html", context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("index"))


# def registration(request):
#     if request.method == "POST":
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse("users:login"))
#     else:
#         form = UserRegistrationForm()
#     context = {"form": form}
#     return render(request, "users/registration.html", context)


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "users/registration.html"
    success_url = reverse_lazy("users:login")
    # success_message = "Вы успешно зарегестрированы!"
    title = "Store - Регистрация"


# @login_required
# def profile(request):
#     if request.method == "POST":
#         form = UserProfileForm(
#             instance=request.user, data=request.POST, files=request.FILES
#         )
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse("users:profile"))
#     else:
#         form = UserProfileForm(instance=request.user)

#     baskets = Basket.objects.filter(user=request.user)
#     context = {
#         "title": "Store - Profile",
#         "form": form,
#         "baskets": baskets,
#         "total_sum": baskets.total_sum(),
#         "total_quantity": baskets.total_quantity(),
#     }
#     return render(request, "users/profile.html", context)


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
