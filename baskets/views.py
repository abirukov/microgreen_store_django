from typing import Any

from django import views
from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers import serialize
from django.http import HttpResponse, HttpRequest
from django.views.generic import DetailView

from baskets.models import Basket, BasketProduct
from products.models import Product


class BasketDetailView(DetailView):
    model = Basket
    template_name = "baskets/detail.html"

    def get_context_data(self, **kwargs: dict[str, Any]) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class BasketProductView(views.View):
    def post(self, request: HttpRequest) -> HttpResponse:
        if not self.check_needle_values():
            return HttpResponse(status=400)

        try:
            product = Product.objects.get(pk=self.request.POST.get("product_id", False))
        except ObjectDoesNotExist:
            return HttpResponse(status=400)

        basket = self.request.user.basket
        if product in basket.products.all():
            basket_product = basket.basketproduct_set.filter(
                product_id=product.id,
            ).first()
            basket_product.quantity = basket_product.quantity + 1
            basket_product.save()
        else:
            BasketProduct(
                basket_id=basket.id,
                product_id=product.id,
                quantity=self.request.POST.get("quantity", False),
                unit_price=product.price,
            ).save()
        data = basket.json()
        return HttpResponse(data, content_type="application/json")

    def update(self, request: HttpRequest) -> HttpResponse:
        if not self.check_needle_values():
            return HttpResponse(status=400)

        try:
            product = Product.objects.get(pk=self.request.POST["product_id"])
        except ObjectDoesNotExist:
            return HttpResponse(status=400)

        basket = self.request.user.basket
        if product in basket.products:
            basket_product = basket.basketproduct_set.filter(
                product_id=product.id,
            ).first()
            basket_product.quantity = self.request.POST["quantity"]
            basket_product.save()
        else:
            BasketProduct(
                basket_id=basket.id,
                product_id=product.id,
                quantity=self.request.POST["quantity"],
                unit_price=product.price,
            ).save()

        basket = Basket.objects.filter(
            user_id=self.request.user.id,
        ).prefetch_related('products').first()
        data = serialize("json", [basket])
        return HttpResponse(data, content_type="application/json")

    def check_needle_values(self):
        return (
            self.request.POST.get("product_id", False)
            and self.request.POST.get("quantity", False)
        )
