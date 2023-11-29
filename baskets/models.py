import json

from django.db import models
from django.utils.translation import gettext_lazy as _
from timestamps.models import SoftDeletes, Timestampable


class Basket(models.Model):
    user = models.OneToOneField(
        "users.User",
        on_delete=models.PROTECT,
        related_name="basket",
    )
    products = models.ManyToManyField("products.Product", through="BasketProduct")

    def __str__(self) -> str:
        return f"{self.user_id}_{self.id}"

    def as_dict(self) -> dict:
        basket_products = self.basketproduct_set.select_related("product").all()
        data = {
            "id": self.id,
            "user_id": self.user_id,
            "products": [],
        }
        total = 0.0
        base_total = 0.0
        for basket_product in basket_products:
            row_sum = float(round(basket_product.quantity * basket_product.unit_price))
            row_base_sum = float(
                round(basket_product.quantity * basket_product.product.price),
            )
            data["products"].append(
                {
                    "id": basket_product.product_id,
                    "title": basket_product.product.title,
                    "quantity": int(basket_product.quantity),
                    "base_price": float(basket_product.product.price),
                    "unit_price": float(basket_product.unit_price),
                    "row_sum": row_sum,
                    "row_base_sum": row_base_sum,
                },
            )
            base_total = base_total + row_base_sum
            total = total + row_sum
        data["base_total"] = base_total
        data["total"] = total
        return data

    def json(self) -> str:
        return json.dumps(self.as_dict())


class BasketProduct(Timestampable, SoftDeletes):
    basket = models.ForeignKey(Basket, on_delete=models.PROTECT)
    product = models.ForeignKey("products.Product", on_delete=models.PROTECT)
    quantity = models.DecimalField(_("quantity"), max_digits=20, decimal_places=2)
    unit_price = models.DecimalField(_("unit_price"), max_digits=20, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.basket_id}_{self.product_id}"
