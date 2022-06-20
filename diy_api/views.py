import logging
from django.shortcuts import render
from rest_framework import generics
from .serializers import GuideSerializer, RegisterSerializer, UserSerializer
# from .serializers import GuideSerializer
from .models import Guide


# added this
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# added these
# from django.http import JsonResponse
# from django.contrib.auth.models import User


# Create your views here.
# added this class
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # testing
        # token['saved'] = user.saved

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class GuideList(generics.ListCreateAPIView):
    queryset = Guide.objects.all().order_by('id')
    serializer_class = GuideSerializer


class GuideDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guide.objects.all().order_by('id')
    serializer_class = GuideSerializer


class RegisterUser(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now Login!",
        })


@api_view(['GET'])
def getUserRoutes(request):
    user_routes = [
        '/token',
        '/token/refresh'
    ]
    return Response(user_routes)
