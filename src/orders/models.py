from django.db import models

# Create your models here.
from account.models import Account
from product.models import Product, Variation


class Payment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    # orderr = models.ForeignKey('Order', models.CASCADE,related_name='order')

    payment_id = models.CharField(max_length=100,blank=True,null=True)
    payment_method = models.CharField(max_length=100,blank=True,null=True)
    amount_paid = models.CharField(max_length=100,blank=True,null=True)
    status = models.CharField(max_length=100,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    order_number = models.CharField(max_length=100)


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
    user = models.ForeignKey(Account, on_delete=models.CASCADE )
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
    status = models.CharField(max_length=100, choices=STATUS, default='Pending')
    ip = models.CharField(blank=True, max_length=20)
    is_order = models.BooleanField(default=False)
    i_agree =models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
    def full_name(self):

        return f'{self.first_name} {self.last_name}'


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation,blank=True)
    # color = models.CharField(max_length=100)
    # size = models.CharField(max_length=100)
    quantity = models.IntegerField()
    product_price = models.IntegerField()
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.product.PRDName
