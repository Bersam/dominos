from django.utils.translation import gettext as _
from rest_framework import serializers

from .models import Order, OrderItem, Customer, Pizza

class PizzaSerializer(serializers.ModelSerializer):
    flavor = serializers.CharField()
    size = serializers.CharField()

    class Meta:
        model = Pizza
        fields = ('flavor', 'size')


class OrderItemSerializer(serializers.ModelSerializer):
    pizza = PizzaSerializer()

    class Meta:
        model = OrderItem
        fields = ('pizza', 'count')

    def validate_count(self, value):
        if value >= 0:
            return value
        else:
            raise serializers.ValidationError(
                _("Count should be non-negative."))


class CustomerSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    phone = serializers.CharField()

    class Meta:
        model = Customer
        fields = ('name', 'phone', 'address')


class OrderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    customer = CustomerSerializer()
    order_items = OrderItemSerializer(
        source='get_items', many=True)
    

    #TODO Set a validation to check state

    class Meta:
        model = Order
        fields = ('id', 'customer', 'order_items', 'state')