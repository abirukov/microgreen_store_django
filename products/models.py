from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    title = models.CharField(_("title"))
    price = models.DecimalField(_("price"), max_digits=20, decimal_places=2)
    description = models.CharField(_("description"), null=True)

    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        related_name="category",
        null=True,
    )
    orders = models.ManyToManyField("Order", through="OrderProduct", related_name="products")
    baskets = models.ManyToManyField("Basket", through="BasketProduct", related_name="products")
