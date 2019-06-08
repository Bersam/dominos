from django.test import TestCase
from ..models import Order, OrderItem, Flavor, Size, Customer


class OrderTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        medium = Size.objects.create(
            name='Medium'
        )
        large = Size.objects.create(
            name='Large'
        )
        pepperoni = Flavor.objects.create(
            name='Pepperoni'
        )
        margherita = Flavor.objects.create(
            name='Margherita'
        )
        customer_1 = Customer.objects.create(
            name="Bersam", phone="+989371268912", address="Tehran/Iran"
        )

        order = Order.objects.create(customer=customer_1)
        order.order_items.create(flavor=pepperoni, size=medium, count=2)
        order.order_items.create(flavor=margherita, size=medium, count=3)
        order.order_items.create(flavor=margherita, size=large, count=1)

    def test_order_details(self):
        customer = Customer.objects.get(name="Bersam")
        order = Order.objects.filter(customer=customer).last()
        self.assertEqual(
            str(order), "Bersam #{0}".format(order.id))
        self.assertEqual(
            order.order_items.count(), 3)
        order.state = "DELIVERED"
        self.assertEqual(
            order.state, "DELIVERED"
        )