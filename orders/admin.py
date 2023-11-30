from django.contrib import admin

from orders.models import Order, OrderProduct, OrderStatus

admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(OrderProduct)
