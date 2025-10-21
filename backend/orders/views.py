from rest_framework import viewsets, permissions
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """CRUD API for orders."""
    queryset = Order.objects.prefetch_related("items", "customer").all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]



class OrderItemViewSet(viewsets.ModelViewSet):
    """CRUD API for order items."""
    queryset = OrderItem.objects.select_related("order", "product").all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.AllowAny]
