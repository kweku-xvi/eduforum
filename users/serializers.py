from .models import User
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8,max_length=100, write_only=True)


    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'name', 'created_at', 'password']

        read_only_fields = ['id']


    def validate(self, attrs):
        email = attrs.get('email')
        username = attrs.get('username')

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('This email is already in use')
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('This username is already in use')

        return attrs

    
    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8,max_length=100, write_only=True)
    

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(username=email, password=password)

        if not user:
            raise serializers.ValidationError('Invalid credentials. Try again', code='authentication')

        attrs['user'] = user
        return attrs


    def generate_tokens(self, attrs):
        user = attrs.get('user')

        refresh = RefreshToken.for_user(user)

        tokens = {
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }

        return tokens


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'name', 'created_at']

        read_only_fields = ['id']
