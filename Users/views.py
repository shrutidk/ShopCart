from django.shortcuts import render
from rest_framework import status, generics,permissions
from rest_framework.response import Response

from .models import User
from Users.serializers import UserSerializer, LoginSerializer
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token

# Create your views here.


class CustomerList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CustomerLoginList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def post(self, request):
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # user = authenticate(username=username, password=password)


        credentials = {
            "username":  request.data.get("username", ""),
            "password": request.data.get("password", ""),
        }

        print(credentials)
        user = authenticate(**credentials)
        token = Token.objects.get(user=user).key

        print(user)
        print(token)
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        #return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response(token)




