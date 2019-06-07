from .views import OrderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', OrderViewSet, basename='order')
urlpatterns = router.urls