from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import (ProductSerializer,CategorySerializer)
from api.models import (Product,Category)

class ListProducts(APIView):
    
    def get(self,request):
        products = Product.objects.all().filter(quantity__gt=0 , is_active=True)
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        product = request.data.get('product')
        serializer = ProductSerializer(data=product)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'success':'Product {} created'.format(serializer.validated_data['name'])})
    