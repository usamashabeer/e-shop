from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.last_name

    def register(self):
        self.save()

    def isExist(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False

    def get_customer_with_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def get_customer_with_id(id):
        try:
            return Customer.objects.get(id=id)
        except:
            return False
