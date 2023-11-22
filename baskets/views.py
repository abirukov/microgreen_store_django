from django.views.generic import DetailView

from baskets.models import Basket


class BasketDetailView(DetailView):
    model = Basket
    template_name = "baskets/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
