from django.contrib import admin

from .models import Customer, Order, Product, Ordercontains, Inventory, Inventorycontains

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Ordercontains)
admin.site.register(Inventory)
admin.site.register(Inventorycontains)
