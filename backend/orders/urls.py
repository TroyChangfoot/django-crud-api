from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, OrderItemViewSet

router = DefaultRouter()
router.register(r"", OrderViewSet, basename="order")
router.register(r"items", OrderItemViewSet, basename="order-item")

urlpatterns = router.urls
