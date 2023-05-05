from django.urls import path, include
from .views import index, products

urlpatterns = [
    path("", index, name="index"),
    path("products/", products, name="products"),
]
