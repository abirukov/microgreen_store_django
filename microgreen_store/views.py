from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View

from products.models import Product


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        products = Product.objects.all()
        return render(
            request,
            "microgreen_store/index.html",
            context={
                "user": request.user,
                "products": products,
            },
        )


class AboutUsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(
            request,
            "microgreen_store/about-us.html",
            context={
                "user": request.user,
            },
        )
