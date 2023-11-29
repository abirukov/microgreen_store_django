from django.contrib.auth.decorators import login_required
from django.urls import path

from baskets.views import BasketDetailView, BasketProductUpdateView, BasketProductView

urlpatterns = [
    path("", login_required(BasketDetailView.as_view()), name="detail"),
    path("product/increment/", login_required(BasketProductView.as_view()), name="increment"),
    path("product/update/", login_required(BasketProductUpdateView.as_view()), name="update"),
]
