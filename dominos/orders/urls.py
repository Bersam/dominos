from .views import OrderViewSet, OrderItemViewSet, CustomerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'orders/(?P<orderid>[^/.]+)/order_item', OrderItemViewSet, basename='order-item')
router.register(r'customers', CustomerViewSet, basename='customer')
urlpatterns = router.urls