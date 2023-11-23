from django.db import models
from django.utils.translation import gettext_lazy as _


class Basket(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.PROTECT,
        related_name="baskets",
    )
    products = models.ManyToManyField("products.Product", through="BasketProduct")

    def __str__(self):
        return f"{self.user_id}_{self.id}"


class BasketProduct(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.PROTECT)
    product = models.ForeignKey("products.Product", on_delete=models.PROTECT)
    quantity = models.DecimalField(_("quantity"), max_digits=20, decimal_places=2)
    unit_price = models.DecimalField(_("unit_price"), max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.basket_id}_{self.product_id}"
