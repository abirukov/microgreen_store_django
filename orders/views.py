from typing import Any

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import DetailView, FormView, TemplateView

from baskets.utils import move_products_from_basket_to_order, clear_basket
from microgreen_store.notifications.telegram import notify_about_order
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

    def form_valid(self, form: OrderCheckoutForm) -> HttpResponseRedirect:
        form_data = form.cleaned_data
        basket_dict = self.request.user.basket.as_dict()
        order = Order.objects.create(
            user=self.request.user,
            comment=form_data["comment"],
            total=basket_dict["total"],
            status=OrderStatus.objects.filter(
                title="Ждет подтверждения"
            ).first()
        )
        move_products_from_basket_to_order(
            basket_dict,
            order.id,
        )
        clear_basket(basket_dict["id"])
        notify_about_order(order)
        self.success_url = f"/orders/after_checkout/{order.id}/"

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['basket'] = self.request.user.basket.as_dict()
        return context


class OrderAfterCheckoutView(TemplateView):
    template_name = "orders/after_checkout.html"

    def get(
        self,
        request: WSGIRequest,
        *args: tuple[Any, ...],
        **kwargs: dict[str, Any],
    ) -> dict[str, Any]:
        order = Order.objects.filter(id=kwargs["id"]).first()
        if not request.user.is_authenticated or request.user.id != order.user_id:
            return redirect("home")

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["order"] = Order.objects.filter(id=kwargs["id"]).first().as_dict()
        return context

