from django.db import models
from django.contrib.auth.models import User


# Create your models here.
COUNT = (
    ('10','10'),
    ('15','15'),
    ('1','1'),
 )
class Product(models.Model):
    date = models.DateField(auto_now_add=False,auto_now=False,blank=True)
    name = models.CharField(max_length=100,null = True)
    suppliers_name = models.CharField(max_length=100,null = True)
    counts = models.CharField(max_length=20,choices = COUNT,null = True)
    manufacturer = models.CharField(max_length=100,null = True)
    quantity = models.PositiveIntegerField(null = True)
    batch_number = models.CharField(max_length=100,null = True)
    expiry_date = models.DateField(auto_now_add=False,auto_now=False,blank=True)
    purchase_rate = models.PositiveIntegerField(null = True)
    mrp_per_unit = models.PositiveIntegerField(null = True)
    rack = models.CharField(max_length=10,null = True)

    class meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return f'{self.name}-{self.quantity}-{self.counts}-{self.manufacturer}-{self.batch_number}-{self.expiry_date}-{self.mrp_per_unit}'

class Order(models.Model):
    date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_set')
    count = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_set')
    vendor = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_set')
    order_quantity = models.PositiveIntegerField(null=True)
    b_number = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_set')
    exp_date = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_set')
    Price_per_unit = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='order_set')

    class meta:
        verbose_name_plural = 'Order'

    def name(self):
        return self.product.name

    def counts(self):
        return self.count.counts

    def manufacturer(self):
        return self.vendor.manufacturer

    def batch_number(self):
        return self.b_number.batch_number

    def expiry_date(self):
        return self.exp_date.expiry_date

    def mrp_per_unit(self):
        return self.price_per_unit.mrp_per_unit

    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'
