from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
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


def page_not_found(request, exception):
    return render(
        request,
        'exceptions.html',
        status=404,
        context={
            "status": 404,
            "description": "Такая страница не найдена",
        },
    )


def forbidden(request, exception):
    return render(
        request,
        'exceptions.html',
        status=403,
        context={
            "status": 403,
            "description": "Доступ запрещен. Попробуйте войти или зарегистрироваться",
        },
    )


def bad_request(request, exception):
    return render(
        request,
        'exceptions.html',
        status=400,
        context={
            "status": 400,
            "description": "Что-то пошло не так, попробуйте заново или напишите нам",
        },
    )


def server_error(request):
    return render(
        request,
        'exceptions.html',
        status=500,
        context={
            "status": 500,
            "description": "Что-то пошло не так, попробуйте заново или напишите нам",
        },
    )
