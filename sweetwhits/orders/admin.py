from django.contrib import admin

# Register your models here.
from .models import Order, OrderItem
# Register your models here.

admin.site.register(Order)
admin.site.register(OrderItem)
