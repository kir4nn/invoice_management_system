from django.db import models

class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True, verbose_name="Customer ID")
    name = models.CharField('Customer/Retailer Name', max_length=50, default='', blank=True, null=True)
    ph_no = models.CharField('Phone Number', max_length=13, default='', blank=True, unique=True)

    def __str__(self):
        return self.name
