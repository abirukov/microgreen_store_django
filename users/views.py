from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from users.forms import RegisterForm, LoginForm


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:account")

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().get(request, *args, **kwargs)

    def form_valid(self, form: RegisterForm) -> HttpResponseRedirect:
        user = form.save()

        if user:
            login(self.request, user)

        return super().form_valid(form)


class AppLoginView(LoginView):
    form_class = LoginForm
    template_name = "users/login.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().get(request, *args, **kwargs)


class AccountView(TemplateView):
    template_name = "users/account.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserOrderList(TemplateView):
    template_name = "users/order_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserAddressView(TemplateView):
    template_name = "users/address.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserDetailView(TemplateView):
    template_name = "users/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

