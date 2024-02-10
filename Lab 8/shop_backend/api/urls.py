from django.urls import path
from api import views

urlpatterns = [
    path('categories/', views.CategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:category_id>/products/', views.ProductListByCategoryAPIView.as_view(), name='products-by-category'),

    path('product/<int:product_id>/buy/', views.ProductBuyAPIView.as_view(), name='product-buy'),
    path('products/',views.ProductAPIView.as_view(),name='create-and-get-products'),

    path('user/<str:id>/orders/',views.UserOrdersView.as_view(), name='user-orders'),

]
