from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from users.views import RegisterView, AccountView, AppLoginView, UserOrderList, UserAddressView

urlpatterns = [
    path("login/", AppLoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("account/", AccountView.as_view(), name="account"),
    path("logout/", LogoutView.as_view(next_page=reverse_lazy('home')), name="logout"),
    path("order_list/", UserOrderList.as_view(), name="order_list"),
    path("address/", UserAddressView.as_view(), name="address"),
]
