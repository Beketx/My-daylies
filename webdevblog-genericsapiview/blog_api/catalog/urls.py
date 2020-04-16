from rest_framework.routers import DefaultRouter

from .views import BallViewSet
router = DefaultRouter()
router.register(r'balls',BallViewSet,basename = 'user')
urlpatterns = router.urls