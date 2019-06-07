from django.utils.translation import gettext as _
from rest_framework import serializers

from .models import Order, OrderItem, Customer


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('flavor', 'size', 'count')

    def to_representation(self, instance):
        rep = super(OrderItemSerializer, self).to_representation(instance)
        rep['flavor'] = instance.flavor.name
        rep['size'] = instance.size.name
        return rep

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
    customer = CustomerSerializer(read_only=True)
    order_items = OrderItemSerializer(
        source='get_items', many=True, read_only=True)
    

    #TODO Set a validation to check state

    class Meta:
        model = Order
        fields = ('id', 'customer', 'order_items', 'state')