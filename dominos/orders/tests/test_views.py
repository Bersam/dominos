import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

from ..models import Order, OrderItem, Size, Flavor, Customer
from ..serializers import OrderSerializer, OrderItemSerializer


# initialize the APIClient app
client = Client()

class GetOrdersTest(TestCase):
    """ Test module for GET all/one order API """

    def setUp(self):
        self.medium = Size.objects.create(name='Medium')
        self.large = Size.objects.create(name='Large')
        self.pepperoni = Flavor.objects.create(name='Pepperoni')
        self.margherita = Flavor.objects.create(name='Margherita')

        self.customer1 = Customer.objects.create(
            name="Bersam", phone="+989371268912", address="Tehran/Iran"
        )

        self.order1 = Order.objects.create(customer=self.customer1, state="SHIPPING")
        self.order1.order_items.create(flavor=self.pepperoni, size=self.medium, count=2)
        self.order1.order_items.create(flavor=self.margherita, size=self.medium, count=3)
        self.order1.order_items.create(flavor=self.margherita, size=self.large, count=1)

        self.order2 = Order.objects.create(customer=self.customer1)
        self.order2.order_items.create(flavor=self.pepperoni, size=self.medium, count=23)
        self.order2.order_items.create(flavor=self.pepperoni, size=self.large, count=34)
        self.order2.order_items.create(flavor=self.margherita, size=self.large, count=11)


    def test_get_all_orders(self):
        # get API response
        response = client.get(reverse('order-list'))
        # get data from db
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_order(self):
        # get API response
        response = client.get(
            reverse('order-detail', kwargs={'pk': self.order1.pk}))
        order = Order.objects.get(pk=self.order1.pk)
        serializer = OrderSerializer(order)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_order(self):
        response = client.get(
            reverse('order-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class UpdateOrdersTest(TestCase):
    """ Test module for UPDATE all/one order API """

    def setUp(self):
        self.medium = Size.objects.create(name='Medium')
        self.large = Size.objects.create(name='Large')
        self.pepperoni = Flavor.objects.create(name='Pepperoni')
        self.margherita = Flavor.objects.create(name='Margherita')

        self.customer1 = Customer.objects.create(
            name="Bersam", phone="+989371268912", address="Tehran/Iran"
        )

        self.order1 = Order.objects.create(customer=self.customer1, state="SHIPPING")
        self.order1.order_items.create(flavor=self.pepperoni, size=self.medium, count=2)
        self.order1.order_items.create(flavor=self.margherita, size=self.medium, count=3)
        self.order1.order_items.create(flavor=self.margherita, size=self.large, count=1)

        self.order2 = Order.objects.create(customer=self.customer1, state="DELIVERED")
        self.order2.order_items.create(flavor=self.margherita, size=self.large, count=1)


    def test_valid_update_count_single_order(self):
        valid_payload = {
            'count': 42,
            'flavor': self.margherita.pk,
        }
        response = client.patch(
            reverse('order-item-detail', kwargs={'orderid': self.order1.pk, 'pk': 0}),
            data=json.dumps(valid_payload),
            content_type='application/json'
        )
        orderitem = self.order1.get_items()[0]
        serializer = OrderItemSerializer(orderitem)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(serializer.data["count"], 42)
        self.assertEqual(serializer.data["flavor"], str(self.margherita))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_count_single_order(self):
        invalid_payload = {
            'count': -1,
        }
        response = client.patch(
            reverse('order-item-detail', kwargs={'orderid': self.order1.pk, 'pk': 0}),
            data=json.dumps(invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delivered_update_count_single_order(self):
        invalid_payload = {
            'count': 4,
        }
        response = client.patch(
            reverse('order-item-detail', kwargs={'orderid': self.order2.pk, 'pk': 0}),
            data=json.dumps(invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)