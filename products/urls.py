from django.contrib.auth.decorators import login_required
from django.urls import path

from products.views import ProductDetailView, ProductListView

urlpatterns = [
    path("list/", login_required(ProductListView.as_view()), name="list"),
    path(
        "<int:product_id>/",
        login_required(ProductDetailView.as_view()),
        name="detail",
    ),
]
