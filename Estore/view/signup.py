from django.shortcuts import render, redirect
from django.contrib.auth import hashers
from Estore.models.customer import Customer
from django.views import View


class Signup(View):
    def post_request(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        password = hashers.make_password(password)
        email = request.POST.get('email')

        value = {'first_name': first_name,
                 'last_name': last_name,
                 'phone': phone,
                 'email': email,
                 'password': password}
        return value

    def validate_fields(self, values):
        if len(values['first_name']) == 0 or len(values['last_name']) == 0 or len(values['phone']) == 0 or len(
                values['email']) == 0 or len(values['password']) == 0:
            return True

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        values = self.post_request(request)
        check = self.validate_fields(values)
        if check:
            error_msg = 'Please filled all the fields'
        else:
            customer = Customer(first_name=values['first_name'],
                                last_name=values['last_name'],
                                phone=values['phone'],
                                password=values['password'],
                                email=values['email'])
            if customer.isExist():
                error_msg = 'Already exist this email !!!'
            else:
                customer.register()
                return redirect('homepage')
        data = {
            'error': error_msg,
            'values': values
        }
        return render(request, 'signup.html', data)
