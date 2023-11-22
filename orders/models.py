from django.db import models
from django.utils.translation import gettext_lazy as _


class OrderStatus(models.Model):
    title = models.CharField(_("title"))


class Order(models.Model):
    comment = models.TextField(_("comment"))
    total = models.DecimalField(_("total"), max_digits=20, decimal_places=2)

    status = models.ForeignKey("OrderStatus", on_delete=models.PROTECT)
    user = models.ForeignKey("User", on_delete=models.PROTECT)
    products = models.ManyToManyField("Product", through="OrderProduct", related_name="orders")
    address = models.ForeignKey(
        "Address",
        on_delete=models.PROTECT,
        null=True,
    )


class OrderProduct(models.Model):
    order = models.ForeignKey("Order", on_delete=models.PROTECT)
    product = models.ForeignKey("Product", on_delete=models.PROTECT)
    quantity = models.DecimalField(_("quantity"), max_digits=20, decimal_places=2)
    unit_price = models.DecimalField(_("unit_price"), max_digits=20, decimal_places=2)
