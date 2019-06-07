from django.contrib import admin

from .models import Order, OrderItem, Pizza, Flavor, Size, Customer

# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('pizza', 'count')

@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ('flavor', 'size')

@admin.register(Flavor)
class FlavorAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name', )
