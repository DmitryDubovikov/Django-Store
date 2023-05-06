from django.shortcuts import render
from products.models import Product, ProductCategory


def index(request):
    context = {"title": "Cool Store"}
    return render(request, "products/index.html", context=context)


def products(request):
    context = {
        "title": "Cool Store: catalog ",
        "products": Product.objects.all(),
        "categories": ProductCategory.objects.all(),
    }
    return render(request, "products/products.html", context=context)
