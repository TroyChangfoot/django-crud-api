from rest_framework import viewsets, permissions
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """CRUD API for products."""
    queryset = Product.objects.all().order_by("-created_at")
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]  # For demo; tighten in prod
