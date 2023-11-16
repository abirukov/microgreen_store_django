from django.contrib.auth import login
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from users.forms import RegisterForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "users/test.html"
    success_url = reverse_lazy("<app_name>:<view_name>")

    def form_valid(self, form):
        user = form.save()

        if user:
            login(self.request, user)

        return super().form_valid(form)

# class UserUpdateView(UpdateView):
#     model = User
#     form_class = UpdateTaskForm
#     template_name = 'users/test.html'
#
#     def get_success_url(self) -> str:
#         task_pk = self.kwargs.get('pk')
#         return reverse('todos:tasks-update', kwargs={'pk': task_pk})


# class UserListView(ListView):
#     model = User
#     template_name = 'users/test.html'
#     context_object_name = 'users'
#
#
# class UserDeleteView(DeleteView):
#     model = User
#     success_url = '/users/'
#     template_name = 'users/test.html'
