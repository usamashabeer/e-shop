from django.db import models
from .category import Category


# Create your models here.
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='', null=True, blank=True)
    # upload_to is used for image saver.
    image = models.ImageField(upload_to='upload/products/')

    # size = models.CharField(max_length=1, choices=STATUS_CHOICES, default='L')

    def __str__(self):
        return self.category.name + ' ' + self.name

    @staticmethod
    def get_all_products_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_product_by_category_id(categoryID):
        if categoryID:
            return Product.objects.filter(category=categoryID)
