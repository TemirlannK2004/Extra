from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from api.models import (Product,Category,Order)
from api.serializers import CategorySerializer,ProductSerializer,OrderSerializer

User = get_user_model()


class ProductAPIView(APIView):

    def get(self,request):
        all_products = Product.objects.all().filter(is_active=True,quantity__gt=0)
        serializer =  ProductSerializer(all_products,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        product = request.data
        serializer = ProductSerializer(data=product)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListByCategoryAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return Product.objects.filter(category_id=category_id)
    

class ProductBuyAPIView(APIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request,product_id,format=None):
        try:
            product_id = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise NotFound('Product Not Found',code=404)

        user = request.user

        order = Order.objects.create(product_id=product_id,user_id = user)
        serializer = OrderSerializer(order)
        return Response(serializer.data,status=status.HTTP_201_CREATED)


class UserOrdersView(APIView):
    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        orders = Order.objects.filter(user_id=id)  
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

