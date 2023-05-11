from django.contrib import admin
from .models import Product,Order
from django.contrib.auth.models import Group

admin.site.site_header = 'AYYPInventory Dashboard'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('date','name','suppliers_name','counts','manufacturer','quantity','batch_number','expiry_date','purchase_rate','mrp_per_unit','rack')
    list_filter = ['counts']
# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
#admin.site.unregister(Group)