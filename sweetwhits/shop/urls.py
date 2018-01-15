from django.urls import path

from . import views

urlpatterns = [
	path('shop/product/<slug:product_slug>/', views.show_product_action, name='product'),
	path('shop/<slug:catagory>/', views.show_product_catagory_action, name='catagory'),
    path('', views.index, name='index'),
]