from django.contrib.auth import login, logout
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.compat import authenticate
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
# from rest_framework.urls import login

from rest_framework.views import APIView

from passport.models import User
from passport.serializers import RegisterSerializers


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializers


class LoginView(APIView):
    def post(self, request):

        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
            else:
                return Response({"error":"用户已被管理员禁止"},status=404)

        else:
            return Response({"error": "用户名或密码错误"}, status=404)

        return Response({"username": user.username, "user_id": user.id})

class LogoutView(APIView):

    def post(self,request):
        logout(request)
        return Response({"mgs":"ok"})
