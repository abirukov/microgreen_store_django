from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from baskets.models import BasketProduct
from products.models import Product


class BasketDetailView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        basket = request.user.basket
        return render(
            request,
            "baskets/detail.html",
            context={
                "user": self.request.user,
                "basket": basket.as_dict(),
            },
        )


class BasketProductView(View):
    def post(self, request: HttpRequest) -> HttpResponse:
        if not check_needle_values(request):
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


class BasketProductUpdateView(View):
    def post(self, request: HttpRequest) -> HttpResponse:
        if not check_needle_values(request):
            return HttpResponse(status=400)

        product_id = self.request.POST.get("product_id", False)
        quantity = self.request.POST.get("quantity", False)

        try:
            product = Product.objects.get(pk=product_id)
        except ObjectDoesNotExist:
            return HttpResponse(status=400)

        basket = self.request.user.basket
        basket_products = basket.products.all()
        if product in basket_products and int(quantity) > 0:
            basket_product = basket.basketproduct_set.filter(
                product_id=product.id,
            ).first()
            basket_product.quantity = quantity
            basket_product.save()
        if product in basket_products and int(quantity) <= 0:
            basket_product = basket.basketproduct_set.filter(
                product_id=product.id,
            ).first()
            basket_product.delete(hard=True)
        else:
            BasketProduct(
                basket_id=basket.id,
                product_id=product.id,
                quantity=quantity,
                unit_price=product.price,
            ).save()
        data = basket.json()
        return HttpResponse(data, content_type="application/json")


def check_needle_values(request: HttpRequest) -> bool:
    return bool(request.POST["product_id"] and request.POST["quantity"])
