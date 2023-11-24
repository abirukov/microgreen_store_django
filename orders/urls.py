from django.urls import path

from orders.views import OrderCheckoutView, OrderDetailView

urlpatterns = [
    path("<int:id>/", OrderDetailView.as_view(), name="detail"),
    path("checkout/<int:id>/", OrderCheckoutView.as_view(), name="detail"),
]
