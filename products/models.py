from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    title = models.CharField(_("title"))
    price = models.DecimalField(_("price"), max_digits=20, decimal_places=2)
    description = models.CharField(_("description"), null=True)

    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        related_name="category",
        null=True,
    )
    # orders = models.ManyToManyField("orders.Order", through="orders.OrderProduct", related_name="products")
    # baskets = models.ManyToManyField("baskets.Basket", through="baskets.BasketProduct", related_name="products")
