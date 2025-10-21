from django.db import models
from django.utils.translation import gettext_lazy as _


class Customer(models.Model):
    """Represents a registered customer or order contact."""

    first_name = models.CharField(_("First Name"), max_length=100)
    last_name = models.CharField(_("Last Name"), max_length=100)
    email = models.EmailField(_("Email"), unique=True)
    phone = models.CharField(_("Phone"), max_length=30, blank=True)
    address = models.CharField(_("Address"), max_length=255, blank=True)
    city = models.CharField(_("City"), max_length=100, blank=True)
    country = models.CharField(_("Country"), max_length=100, blank=True)
    created_at = models.DateTimeField(_("Created"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated"), auto_now=True)

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
