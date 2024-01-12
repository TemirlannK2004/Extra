from django.urls import path,include

from api.views import ListProducts


urlpatterns = [
    path('all_products/',ListProducts.as_view(),name='all_products'),
]
