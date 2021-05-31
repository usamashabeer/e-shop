"""Eshop URL Configuration

The `urlpatterns` list routes URLs to view. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function view
    1. Add an import:  from my_app import view
    2. Add a URL to urlpatterns:  path('', view.home, name='home')
Class-based view
    1. Add an import:  from other_app.view import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Estore.view import signup, login, index, cartview, checkout, orderview

urlpatterns = [
    path('', index.Index.as_view(), name='homepage'),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('logi', login.Login.as_view(), name='login'),
    path('logout', login.logout, name='logout'),
    path('order', orderview.OrderView.as_view(), name='order'),
    path('cart', cartview.CartView.as_view(), name='cart'),
    path('check-out', checkout.Checkout.as_view(), name='checkout'),
]
