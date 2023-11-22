from django.db import models
from django.utils.translation import gettext_lazy as _


class Address(models.Model):
    city = models.CharField(_("city"), max_length=255)
    street = models.CharField(_("street"), max_length=255)
    house = models.CharField(_("house"), max_length=10, null=True)
    apartment = models.CharField(_("apartment"), max_length=10, null=True)
    comment = models.TextField(_("comment"), null=True)
    user = models.ForeignKey("User", on_delete=models.PROTECT)
