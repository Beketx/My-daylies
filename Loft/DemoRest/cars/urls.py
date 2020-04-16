from django.urls import path
from cars.views import CarCreateView
app_name = 'car'
urlpatterns = [
    path('car/create/', CarCreateView.as_view())
]   