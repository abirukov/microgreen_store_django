from django.db import models
from django.utils.translation import gettext_lazy as _
from timestamps.models import SoftDeletes, Timestampable


class Product(Timestampable, SoftDeletes):
    title = models.CharField(_("title"))
    price = models.DecimalField(_("price"), max_digits=20, decimal_places=2)
    description = models.CharField(_("description"), null=True)
    image = models.ImageField(upload_to="images/product", null=True)

    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        related_name="category",
        null=True,
    )

    def __str__(self) -> str:
        return self.title
