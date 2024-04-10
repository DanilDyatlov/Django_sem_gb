from django.db import models
from django.core.validators import RegexValidator


class Customer(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone_number = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True)
    time_stamp_on_create = models.DateTimeField()

    def __str__(self):
        return f'{self.username}, {self.email}, {self.phone_number}'


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    time_stamp_on_create = models.DateTimeField()
    img = models.ImageField(blank=True)

    def __str__(self):
        return f'{self.title}, {self.price}'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    time_stamp_on_create = models.DateTimeField()

    def __str__(self):
        return f'{self.customer.username}, total: {self.total}'
