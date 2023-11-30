from django.db import models
from timestamps.models import SoftDeletes, Timestampable


class FaqQuestion(Timestampable, SoftDeletes):
    question = models.CharField("question")
    answer = models.CharField("answer")
    is_published = models.BooleanField("is_published")

    def __str__(self) -> str:
        return self.question[:20]
