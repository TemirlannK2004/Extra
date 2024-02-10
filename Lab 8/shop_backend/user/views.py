from rest_framework import generics
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.contrib.auth import get_user_model

from user import serializers

User = get_user_model()

class RegisterUserView(generics.CreateAPIView):
    serializer_class = serializers.RegisterUserSerializer
    parser_classes = [JSONParser, MultiPartParser, FormParser]

    def create(self,request,*args, **kwargs):
        if User.objects.filter(username = request.data.get('username')).exists():
            return Response(
                {'error':'Username already exists!'},
                status=status.HTTP_400_BAD_REQUEST
                )
        return super().create(request,*args, **kwargs)
    

class LoginView(APIView):
    def post(self,request):
        serializer_class = serializers.LoginUserSerializer     
        serializer = serializer_class(data=request.data,context = {'request':request})
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

