from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(_("title"))
    products = models.ForeignKey("Product", on_delete=models.PROTECT)
