from django.urls import path

from baskets.views import BasketDetailView, BasketProductUpdateView, BasketProductView

urlpatterns = [
    path("", BasketDetailView.as_view(), name="detail"),
    path("product/increment/", BasketProductView.as_view(), name="increment"),
    path("product/update/", BasketProductUpdateView.as_view(), name="update"),
]
