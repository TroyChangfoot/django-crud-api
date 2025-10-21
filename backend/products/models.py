from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    """Represents an item available for purchase or inventory tracking."""

    name = models.CharField(_("Name"), max_length=255)
    description = models.TextField(_("Description"), blank=True)
    sku = models.CharField(_("SKU"), max_length=50, unique=True)
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(_("Stock"), default=0)
    is_active = models.BooleanField(_("Active"), default=True)
    created_at = models.DateTimeField(_("Created"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated"), auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return f"{self.name} ({self.sku})"
