from django.contrib import admin

from .models import Catagory, Product, ProductVariation, ProductAttribute
# Register your models here.

admin.site.register(Catagory)
admin.site.register(Product)
admin.site.register(ProductVariation)
admin.site.register(ProductAttribute)