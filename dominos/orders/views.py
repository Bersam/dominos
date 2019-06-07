from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer

# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for listing or retrieving orders.
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


#TODO Create a View for modifiying OrderItems of an item
#TODO Create a View for modifiying Customers