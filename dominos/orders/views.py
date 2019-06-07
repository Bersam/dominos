from django.utils.translation import ugettext_lazy as _

from rest_framework import viewsets
from rest_framework.exceptions import NotFound

from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer


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
        order = Order.objects.get(id=orderid)
        pk = int(self.kwargs.get("pk", False))

        try:
            return OrderItem.objects.filter(order=order)[pk-1]
        except (OrderItem.DoesNotExist, IndexError, AssertionError):
            raise NotFound(_("OrderItem not found."))


#TODO Create a View for modifiying Customers
