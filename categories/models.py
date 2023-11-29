from django.db import models
from django.utils.translation import gettext_lazy as _
from timestamps.models import SoftDeletes, Timestampable


class Category(Timestampable, SoftDeletes):
    title = models.CharField(_("title"))

    def __str__(self) -> str:
        return self.title
