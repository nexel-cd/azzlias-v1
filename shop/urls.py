from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('category/<pk>', views.shop_category, name='category_details'),
    path('products/<pk>', views.product_details, name='product_details'),
] 
