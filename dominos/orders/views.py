from django.utils.translation import ugettext_lazy as _

from rest_framework import viewsets
from rest_framework.exceptions import NotFound

from .models import Order, OrderItem, Customer
from .serializers import OrderSerializer, OrderItemSerializer, CustomerSerializer


# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for listing or retrieving orders.
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderItemViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for listing or retrieving orders.
    """
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        orderid = self.kwargs.get("orderid", False)
        order = Order.objects.get(id=orderid)

        try:
            return OrderItem.objects.filter(order=order)
        except OrderItem.DoesNotExist:
            raise NotFound(_("OrderItem not found."))

    def get_object(self):
        orderid = self.kwargs.get("orderid", False)
        pk = int(self.kwargs.get("pk", False))

        try:
            order = Order.objects.get(id=orderid)
            return OrderItem.objects.filter(order=order)[pk-1]
        except (OrderItem.DoesNotExist, IndexError, AssertionError):
            raise NotFound(_("Order not found."))

    def perform_create(self, serializer):
        orderid = self.kwargs.get("orderid", False)
        pk = int(self.kwargs.get("pk", False))

        try:
            order = Order.objects.get(id=orderid)
            order_item = serializer.save()
            order.order_items.add(order_item)
            order.save()
            return OrderItem.objects.filter(order=order)
        except (Order.DoesNotExist):
            raise NotFound(_("Order not found."))
