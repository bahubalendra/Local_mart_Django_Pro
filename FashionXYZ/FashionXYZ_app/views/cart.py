from django.shortcuts import render, redirect
from FashionXYZ_app.models.customer import Customer
from FashionXYZ_app.models.product import Product
from django.contrib.auth.hashers import check_password
from django.views import View


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products} )


