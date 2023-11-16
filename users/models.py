from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    phone = models.CharField(_("phone"), max_length=20, null=True)
    tg_id = models.CharField(_("tg_id"), max_length=20, null=True)
    tg_username = models.CharField(_("tg_username"), max_length=50, null=True)
    personal_code = models.CharField(_("personal_code"), max_length=10, null=True)
    referrer = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
