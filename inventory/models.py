from django.db import models

class Inventory(models.Model):
    product_number = models.IntegerField(primary_key=True)
    product = models.TextField(max_length=3000, default='', blank=True, null=True)
    title = models.CharField('Title', max_length=120, default='', blank=True, null=True, unique=True)
    amount = models.IntegerField('Unit Price', default=0, blank=True, null=True)

    def __str__(self):
        return self.title
