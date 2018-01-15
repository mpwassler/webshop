from django.db import models
from shop.models import Product, ProductVariation
# Create your models here.
class Order(models.Model):
	date = models.DateTimeField()
	total = models.DecimalField(max_digits=5,decimal_places=2)
	shipping_address_1 = models.CharField(max_length=260)
	shipping_address_2 = models.CharField(max_length=260)
	shipping_postcode = models.CharField(max_length=10)
	shipping_city = models.CharField(max_length=260)
	shipping_state = models.CharField(max_length=3)
	billing_address_1 = models.CharField(max_length=260)
	billing_address_2 = models.CharField(max_length=260)
	billing_postcode = models.CharField(max_length=10)
	billing_city = models.CharField(max_length=260)
	billing_state = models.CharField(max_length=3)
	customer_phone = models.CharField(max_length=20)
	customer_email = models.EmailField(max_length=254)

class OrderItem(models.Model):
	cost = models.DecimalField(max_digits=5,decimal_places=2)
	quantity = models.IntegerField()
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	product_variation = models.ForeignKey(ProductVariation, on_delete=models.CASCADE)
