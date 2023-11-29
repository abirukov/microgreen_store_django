from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from users.views import AccountView, AppLoginView, RegisterView, UserAddressView, UserOrderList

urlpatterns = [
    path("login/", AppLoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("account/", login_required(AccountView.as_view()), name="account"),
    path("logout/", login_required(LogoutView.as_view(next_page=reverse_lazy("home"))), name="logout"),
    path("order_list/", login_required(UserOrderList.as_view()), name="order_list"),
    path("address/", login_required(UserAddressView.as_view()), name="address"),
]
