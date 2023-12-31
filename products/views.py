from typing import Any

from django.views.generic import DetailView, ListView

from products.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "products/list.html"
    context_object_name = "products"
    paginate_by = 8

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/detail.html"
    pk_url_kwarg = "product_id"
    context_object_name = "product"

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
