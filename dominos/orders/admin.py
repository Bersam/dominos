from django.contrib import admin

from .models import Order, OrderItem, Flavor, Size, Customer

# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'get_orders')

    def get_orders(self, obj):
        return ",\n".join([str(order_item) for order_item in obj.order_items.all()])

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('flavor', 'size', 'count')

@admin.register(Flavor)
class FlavorAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name', )
