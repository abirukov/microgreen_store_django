from django.contrib.auth.decorators import login_required
from django.urls import path

from orders.views import OrderCheckoutView, OrderDetailView, OrderAfterCheckoutView

urlpatterns = [
    path("<int:id>/", login_required(OrderDetailView.as_view()), name="detail"),
    path("checkout/", login_required(OrderCheckoutView.as_view()), name="checkout"),
    path("after_checkout/<int:id>/", login_required(OrderAfterCheckoutView.as_view()), name="after_checkout"),
]
