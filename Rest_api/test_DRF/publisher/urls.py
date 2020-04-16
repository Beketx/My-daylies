from django.urls import path
from publisher.views import AuthorView



urlpatterns = [
    path('authors/',AuthorView.as_view())
]