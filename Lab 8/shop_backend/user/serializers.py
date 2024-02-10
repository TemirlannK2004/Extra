from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers



User = get_user_model()


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name')


class RegisterUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50,min_length=3)
    password = serializers.CharField(max_length=68,min_length=8,write_only=True)
    re_password = serializers.CharField(max_length=68,min_length=8,write_only=True)

    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','password','re_password')

    def validate(self, attrs):
        password = attrs.get('password','')
        re_password = attrs.get('re_password','')

        if password!=re_password:
            raise serializers.ValidationError('Passwords Should be equal! Please check again')
        return attrs

    def create(self,validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            password = validated_data['password']
        )
        return user
    

class LoginUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50,min_length=3)
    password = serializers.CharField(max_length=68,min_length=8,write_only=True)
    first_name = serializers.CharField(max_length = 150,read_only=True)
    last_name = serializers.CharField(max_length = 150,read_only=True)
    access_token = serializers.CharField(max_length=255,read_only=True)
    refresh_token = serializers.CharField(max_length=255,read_only=True)

    class Meta:
        model = User
        fields = ('username','password','first_name','last_name','access_token','refresh_token')

    def validate(self, attrs):
        username = attrs.get('username') 
        password = attrs.get('password') 
        request = self.context.get('request')  
        user = authenticate(request,username=username,password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials')
        user_token = user.tokens()
        
        return ({
            'username':user.username,
            'first_name':user.first_name,
            'last_name':user.last_name,
            'access_token':str(user_token.get('access')),
            'refresh_token':str(user_token.get('refresh')),
        })