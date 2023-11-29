"""
URL configuration for microgreen_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path

from faq_questions.views import FaqView
from microgreen_store import settings
from microgreen_store.views import AboutUsView, IndexView, page_not_found, bad_request, forbidden, server_error

handler400 = bad_request
handler403 = forbidden
handler404 = page_not_found
handler500 = server_error

urlpatterns = [
    path("", login_required(IndexView.as_view()), name="home"),
    path("about/", login_required(AboutUsView.as_view()), name="about"),
    path("faq/", login_required(FaqView.as_view()), name="faq"),
    path("users/", include(("users.urls", "users"), namespace="users")),
    path("products/", include(("products.urls", "products"), namespace="products")),
    path("baskets/", include(("baskets.urls", "baskets"), namespace="baskets")),
    path("orders/", include(("orders.urls", "orders"), namespace="orders")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


