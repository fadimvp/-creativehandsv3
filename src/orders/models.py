from django.db import models

# Create your models here.
from account.models import Account
from product.models import Product, Variation


class Payment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    amount_paid = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_id


class Order(models.Model):
    STATUS = (
        ('default', 'default'),
        ('Pending', 'Pending'),
        ('Under_Process', 'Under_Process'),
        ('Completed', 'Completed'),
        ('Canceld', 'Canceld'),
        ('Rejected', 'Rejected'),

    )
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True)
    order_number = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    order_note = models.CharField(max_length=100)
    total = models.FloatField()
    tax = models.FloatField()
    status = models.CharField(max_length=100, choices=STATUS, default='default')
    ip = models.CharField(blank=True, max_length=20)
    is_order = models.BooleanField(default=False)
    i_agree =models.BooleanField(default=False)

    def __str__(self):
        return self.first_name
    def full_name(self):

        return f'{self.first_name} {self.last_name}'


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    variation = models.ForeignKey(Variation, on_delete=models.SET_NULL, null=True)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    quantity = models.IntegerField()
    product_price = models.CharField(max_length=100)


    def __str__(self):
        return self.product.PRDName
