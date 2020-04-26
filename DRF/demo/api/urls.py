from django.urls import path

# from api.views import category_list, category_detail

# from api.views.views_cbv import CategoryListAPIView,CategoryDetailAPIView

# from api.views.views_generics import CategoryListAPIView

from api.views.views_generics_better import CategoryListAPIView, CategoryDetailAPIView, ProductListAPIView, ProductDetailAPIView, CategoryWithProductsAPIView
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    # views_FBC
    # path('categories/', category_list),
    # path('categories/<int:category_id>/', category_detail),

    # path('categories/<int:category_id>/products/', category_products),

    #views_CBV
    # path('categories/', CategoryListAPIView.as_view()),
    # path('categories/<int:category_id>/', CategoryDetailAPIView.as_view()),

    #views_generics
    # path('categories/', CategoryListAPIView.as_view()),
    path('login/', obtain_jwt_token),
    path('categories/', CategoryWithProductsAPIView.as_view()),
    path('categories/<int:category_id>/', CategoryDetailAPIView.as_view()),
    path('products/', ProductListAPIView.as_view()),
    path('products/<int:pk>/', ProductDetailAPIView.as_view()),
    path('categorieswith/', CategoryWithProductsAPIView.as_view()),
     
]
