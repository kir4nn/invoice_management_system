from django.contrib import admin
from .models import Inventory
from .forms import InventoryForm

class InventoryAdmin(admin.ModelAdmin):
   list_display = ['title', 'product_number']
   form = InventoryForm
   list_filter = ['title']
   search_fields = ['title', 'product_number']

admin.site.register(Inventory, InventoryAdmin)
