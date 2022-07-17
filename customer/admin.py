from django.contrib import admin
from .models import Customer
from .forms import CustomerForm
class CustomerAdmin(admin.ModelAdmin):
   list_display = ['customer_id', 'name']
   form = CustomerForm
   list_filter = ['name']
   search_fields = ['customer_id', 'name']

admin.site.register(Customer, CustomerAdmin)
