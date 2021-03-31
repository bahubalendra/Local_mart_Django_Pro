from django.shortcuts import render, redirect
from FashionXYZ_app.models.customer import Customer
from FashionXYZ_app.models.customer import Customer
from FashionXYZ_app.middleware.auth import auth_middleware

from FashionXYZ_app.models.orders import Order
from django.contrib.auth.hashers import check_password
from django.views import View



class OrderView(View):

    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request, 'orders.html', {'orders': orders})




