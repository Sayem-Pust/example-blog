from django.shortcuts import render, get_object_or_404
from .serializers import UserCreateSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from authentication.models import User
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserCreateSerializer
from .permissions import IsOwnerOrReadOnly

class Login(ListCreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.filter(is_active=True)

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user_instance = get_object_or_404(User, email=email)
        if user_instance:
            refresh = RefreshToken.for_user(user_instance)
            return Response(
                {
                    'message': 'login successfull',
                    'data': {
                        'user': UserCreateSerializer(user_instance).data,
                        'refresh': str(refresh),
                        'access': str(refresh.access_token)
                    }
                },
                status=status.HTTP_201_CREATED
            )

        else:
            return Response(
                {
                    'message': 'login failed',
                },
                status=status.HTTP_400_BAD_REQUEST
            )


class Registration(ListCreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def post(self, request):
        user_serializer = UserCreateSerializer(data=request.data)
        if user_serializer.is_valid():
            user_instance = user_serializer.save()
            refresh=RefreshToken.for_user(user_instance)
            return Response(
                {
                    'message': 'registration successful',
                    'data': {
                        'user': user_serializer.data,
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    }
                },
                status=status.HTTP_201_CREATED
            )

        else:
            return Response(
                {
                    'message': 'registration failed',
                    'error': user_serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST
            )
