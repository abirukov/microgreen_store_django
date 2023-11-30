import json

from django.db import models
from django.utils.translation import gettext_lazy as _
from timestamps.models import SoftDeletes, Timestampable


class OrderStatus(Timestampable, SoftDeletes):
    title = models.CharField(_("title"))

    def __str__(self) -> str:
        return self.title


class Order(Timestampable, SoftDeletes):
    comment = models.TextField(_("comment"))
    total = models.DecimalField(_("total"), max_digits=20, decimal_places=2)

    status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT)
    user = models.ForeignKey("users.User", on_delete=models.PROTECT)
    products = models.ManyToManyField("products.Product", through="OrderProduct")
    address = models.ForeignKey(
        "addresses.Address",
        on_delete=models.PROTECT,
        null=True,
    )

    def as_dict(self) -> dict:
        order_products = self.orderproduct_set.select_related("product").all()
        data = {
            "id": self.id,
            "user_id": self.user_id,
            "products": [],
        }
        total = 0.0
        base_total = 0.0
        for order_product in order_products:
            row_sum = float(round(order_product.quantity * order_product.unit_price))
            row_base_sum = float(
                round(order_product.quantity * order_product.product.price),
            )
            data["products"].append(
                {
                    "id": order_product.product_id,
                    "title": order_product.product.title,
                    "quantity": int(order_product.quantity),
                    "base_price": float(order_product.product.price),
                    "unit_price": float(order_product.unit_price),
                    "row_sum": row_sum,
                    "row_base_sum": row_base_sum,
                    "image_url": order_product.product.image.url
                    if order_product.product.image
                    else None,
                },
            )
            base_total = base_total + row_base_sum
            total = total + row_sum
        data["base_total"] = base_total
        data["total"] = total
        return data

    def json(self) -> str:
        return json.dumps(self.as_dict())

    def __str__(self) -> str:
        return f"{self.user_id}_{self.id}"


class OrderProduct(Timestampable, SoftDeletes):
    order = models.ForeignKey("orders.Order", on_delete=models.PROTECT)
    product = models.ForeignKey("products.Product", on_delete=models.PROTECT)
    quantity = models.DecimalField(_("quantity"), max_digits=20, decimal_places=2)
    unit_price = models.DecimalField(_("unit_price"), max_digits=20, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.order_id}_{self.product_id}"
