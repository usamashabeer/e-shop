from django.shortcuts import render, redirect
from django.contrib.auth import hashers
from Estore.models.customer import Customer
from django.views import View


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        if len(email) == 0 or len(password) == 0:
            error_msg = 'Please fill both fields'
        else:
            customer = Customer.get_customer_with_email(email)

            if customer:
                if hashers.check_password(password, customer.password):
                    request.session['customer'] = customer.id

                    return redirect('/')
                else:
                    error_msg = "Email or Password are wrong!!"

        return render(request, 'login.html', {'error': error_msg})


def logout(request):
    request.session.clear()
    return redirect('login')