from django.db import models
from django.utils.translation import gettext_lazy as _
from customers.models import Customer
from products.models import Product


class Order(models.Model):
    """Represents a customer order."""

    class Status(models.TextChoices):
        PENDING = "pending", _("Pending")
        PAID = "paid", _("Paid")
        SHIPPED = "shipped", _("Shipped")
        CANCELLED = "cancelled", _("Cancelled")

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    status = models.CharField(_("Status"), max_length=20, choices=Status.choices, default=Status.PENDING)
    total_amount = models.DecimalField(_("Total Amount"), max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(_("Created"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated"), auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return f"Order #{self.pk} - {self.customer}"


class OrderItem(models.Model):
    """Line items belonging to an order."""

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(_("Quantity"), default=1)
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    def get_line_total(self):
        return self.quantity * self.price
