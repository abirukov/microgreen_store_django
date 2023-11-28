from django.urls import path

from baskets.views import BasketDetailView, BasketProductView

urlpatterns = [
    path("<int:id>/", BasketDetailView.as_view(), name="detail"),
    path("product/", BasketProductView.as_view(), name="product"),
]
