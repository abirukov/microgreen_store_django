from django.db import models
from django.utils.translation import gettext_lazy as _
from timestamps.models import SoftDeletes, Timestampable


class Address(Timestampable, SoftDeletes):
    city = models.CharField(_("city"), max_length=255)
    street = models.CharField(_("street"), max_length=255)
    house = models.CharField(_("house"), max_length=10, null=True)
    apartment = models.CharField(_("apartment"), max_length=10, null=True)
    comment = models.TextField(_("comment"), null=True)
    user = models.ForeignKey("users.User", on_delete=models.PROTECT)
