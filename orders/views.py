from typing import Any

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView

from baskets.utils import move_products_from_basket_to_order, clear_basket
from orders.forms import OrderCheckoutForm
from orders.models import Order, OrderStatus


class OrderDetailView(DetailView):
    model = Order
    template_name = "orders/detail.html"

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class OrderCheckoutView(FormView):
    form_class = OrderCheckoutForm
    template_name = "orders/checkout.html"
    success_url = reverse_lazy("orders:after_checkout")

    def form_valid(self, form: OrderCheckoutForm) -> HttpResponseRedirect:
        basket_dict = self.request.user.basket.as_dict()
        order = Order(
            user=self.request.user,
            comment=form.comment,
            total=basket_dict["total"],
            status=OrderStatus.objects.filter(
                title="Ждет подтверждения"
            ).first()
        ).save()
        move_products_from_basket_to_order(
            basket_dict,
            order.id,
        )
        clear_basket(basket_dict["id"])

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['basket'] = self.request.user.basket.as_dict()
        return context
