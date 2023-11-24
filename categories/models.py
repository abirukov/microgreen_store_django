from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(_("title"))

    def __str__(self) -> str:
        return self.title
