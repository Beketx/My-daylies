#so this is a implement of APIView
'''
from django.urls import path
from delivery.views import ConsumerView
app_name = 'delirvery'

urlpatterns = [
    path('consumers/', ConsumerView.as_view()),
    path('consumers/<int:pk>',ConsumerView.as_view())
]
'''

#After add SingleConsumerview
'''
from django.urls import path
from .views import ArticleView, SingleArticleView
app_name = "articles"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('articles/<int:pk>', SingleArticleView.as_view()),
]
'''

#AFter viewset
'''
from django.urls import path
from .views import ArticleView
app_name = "articles"
urlpatterns = [
    path('articles/', ConsumerView.as_view({'get':'list'})),
    path('articles/<int:pk>', ConsumerView.as_view({'get': 'retrieve'}))
]
'''


#AFter VIEWSET 2.0
'''
from rest_framework.routers import DefaultRouter
from .views import ConsumerView
router = DefaultRouter()
router.register(r'consumers',ConsumerView,basename='player')
urlpatterns = router.urls
'''

#After the last VIEWSET
'''
from rest_framework.routers import DefaultRouter
from. views import ConsumerViewSet
router = DefaultRouter()
router.register(r'consumers',ConsumerView, basename = 'player')
urlpatterns=router.urls
'''