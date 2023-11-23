from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from faq_questions.models import FaqQuestion


class FaqView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        questions = FaqQuestion.objects.filter(is_published=True)
        return render(
            request,
            "microgreen_store/faq.html",
            context={
                "user": request.user,
                "questions": questions,
            }
        )
