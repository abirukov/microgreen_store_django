from django.contrib.auth.decorators import login_required
from django.urls import path

from orders.views import OrderCheckoutView, OrderDetailView

urlpatterns = [
    path("<int:id>/", login_required(OrderDetailView.as_view()), name="detail"),
    path("checkout/", login_required(OrderCheckoutView.as_view()), name="checkout"),
]
