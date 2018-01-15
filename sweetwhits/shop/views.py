from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from .models import Catagory, Product

def index(request):
    return render(request, 'shop/catagory.html')

def show_product_catagory_action(request, catagory):
	catagory = Catagory.objects.get(slug=catagory)
	products = Product.objects.filter(catagory_id=catagory.id)

	return render(request, 'shop/catagory.html', {
		'title' : catagory.title,
		'slug' : catagory.slug,
		'products' : products
	})

def show_product_action(request, product_slug):
	return render(request, 'shop/single.html')	