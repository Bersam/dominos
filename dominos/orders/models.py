from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.utils import timezone


class Flavor(models.Model):
    name = models.CharField(_("Flavor Name"), max_length=50)    


    class Meta:
        verbose_name = _("Flavor")
        verbose_name_plural = _("Flavors")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("flavor_detail", kwargs={"pk": self.pk})


class Size(models.Model):
    name = models.CharField(_("Size Name"), max_length=50)


    class Meta:
        verbose_name = _("Size")
        verbose_name_plural = _("Sizes")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("size_detail", kwargs={"pk": self.pk})


class Pizza(models.Model):
    size = models.ForeignKey(Size, verbose_name=_("Size"), on_delete=models.CASCADE)
    flavor = models.ForeignKey(Flavor, verbose_name=_("Flavor"), on_delete=models.CASCADE)


    class Meta:
        verbose_name = _("Pizza")
        verbose_name_plural = _("Pizzas")

    def __str__(self):
        return self.flavor.name

    def get_absolute_url(self):
        return reverse("pizza_detail", kwargs={"pk": self.pk})


class Customer(models.Model):
    name = models.CharField(_("Customer Name"), max_length=50)
    address = models.TextField(_("Address"))
    phone = models.CharField(_("Phone"), max_length=15)
    

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("customer_detail", kwargs={"pk": self.pk})


class OrderItem(models.Model):
    pizza = models.ForeignKey(Pizza, verbose_name=_("Pizza"), on_delete=models.CASCADE)
    count = models.IntegerField(_("count"))
    

    class Meta:
        verbose_name = _("OrderItem")
        verbose_name_plural = _("OrderItems")

    def __str__(self):
        return self.pizza.name

    def get_absolute_url(self):
        return reverse("orderItem_detail", kwargs={"pk": self.pk})


class Order(models.Model):
    order_items = models.ManyToManyField(OrderItem, verbose_name=_("Order Items"))
    customer = models.ForeignKey(Customer, verbose_name=_("Customer"), on_delete=models.CASCADE)
    STATE_CHOICES = (
        ("PROCESSING", _("Your order is being processed")),
        ("COOKING", _("Restaurant is preparing your order")),
        ("SHIPPING", _("Shipping from Restaurant to the Customer")),
        ("DELIVERED", _("Delivered to the Customer")),
    )
    state = models.CharField(choices=STATE_CHOICES, max_length=15, null=True, blank=True)


    created = models.DateTimeField(_("Order Date"), editable=False, default=timezone.now)
    modified = models.DateTimeField(_("Order Update Date"), default=timezone.now)


    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return "{0} #{1}".format(self.customer.name, self.pk)

    def get_absolute_url(self):
        return reverse("order_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Order, self).save(*args, **kwargs)
