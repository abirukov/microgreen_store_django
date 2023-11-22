from django.views.generic import DetailView

from orders.models import Order


class OrderDetailView(DetailView):
    model = Order
    template_name = "orders/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class OrderCheckoutView(DetailView):
    model = Order
    template_name = "orders/checkout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
