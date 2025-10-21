from rest_framework import viewsets, permissions
from .models import Customer
from .serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """CRUD API for customers."""
    queryset = Customer.objects.all().order_by("last_name")
    serializer_class = CustomerSerializer
    permission_classes = [permissions.AllowAny]
