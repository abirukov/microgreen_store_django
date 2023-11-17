from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import RegisterForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "users/test.html"
    success_url = reverse_lazy("<app_name>:<view_name>")

    def form_valid(self, form: RegisterForm) -> HttpResponseRedirect:
        user = form.save()

        if user:
            login(self.request, user)

        return super().form_valid(form)
