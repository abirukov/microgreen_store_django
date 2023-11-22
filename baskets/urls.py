from django.urls import path

from baskets.views import BasketDetailView

urlpatterns = [
    path("<int:id>/", BasketDetailView.as_view(), name="detail"),
]
