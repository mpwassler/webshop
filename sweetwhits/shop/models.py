from django.db import models

# Create your models here.
class Catagory(models.Model):
	title = models.CharField(max_length=260)
	def __str__(self):
		return self.title

class Product(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
	def __str__(self):
		return self.title

class ProductImage(models.Model):
	link = models.TextField()
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	def __str__(self):
		return self.link

class ProductVariation(models.Model):
	sku = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=5,decimal_places=2)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	def __str__(self):
		return self.title

class ProductAttribute(models.Model):
	product_variation = models.ForeignKey(ProductVariation, on_delete=models.CASCADE)
	attribute_title = models.CharField(max_length=260)
	attribute_value = models.CharField(max_length=260)
	def __str__(self):
		return self.attribute_title
