from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "microgreen_store/index.html")
