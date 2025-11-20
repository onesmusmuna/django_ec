from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.add_product, name='add_product'),
]
