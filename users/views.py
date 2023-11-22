from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from users.forms import RegisterForm, LoginForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:account")

    def form_valid(self, form: RegisterForm) -> HttpResponseRedirect:
        user = form.save()

        if user:
            login(self.request, user)

        return super().form_valid(form)


class AppLoginView(LoginView):
    form_class = LoginForm
    template_name = "users/login.html"


class AccountView(TemplateView):
    template_name = "users/account.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
