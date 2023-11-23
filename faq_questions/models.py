from django.db import models


class FaqQuestion(models.Model):
    question = models.CharField("question")
    answer = models.CharField("answer")
    is_published = models.BooleanField("is_published")

    def __str__(self):
        return self.question[:20]
