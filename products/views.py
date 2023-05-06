from django.shortcuts import render


def index(request):
    context = {"title": "Cool Store"}
    return render(request, "products/index.html", context=context)


def products(request):
    context = {"title": "Cool Store: catalog "}
    return render(request, "products/products.html", context=context)
