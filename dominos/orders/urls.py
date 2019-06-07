from .views import OrderViewSet, OrderItemViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', OrderViewSet, basename='order')
router.register(r'(?P<orderid>[^/.]+)/order_item', OrderItemViewSet, basename='order-item')
urlpatterns = router.urls