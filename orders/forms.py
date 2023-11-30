from django import forms
from django.forms import Form

from orders.models import Order


class OrderCheckoutForm(Form):
    comment = forms.CharField(
        widget=forms.Textarea(),
        label="Комментарий",
    )

    class Meta:
        model = Order
        fields = ["comment"]
