from .serializers import *
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(["POST"])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response(status=status.HTTP_200_OK)
        # return redirect('/home')
    
    messages.info(request, "Username or password is incorrect")
    return Response(status=status.HTTP_400_BAD_REQUEST)
    # serialized_data = loginSerializer(data=request.data)
    # if serialized_data.is_valid(raise_exception=True):
    #     try:
    #         user = User.get_user_by_email(email=serialized_data.validated_data['email'])
    #         if user.password != serialized_data.validated_data['password']:
    #             return Response(data={'message': 'wrong password'}, status=status.HTTP_400_BAD_REQUEST)
    #         return Response(data={'message': 'ok'}, status=status.HTTP_200_OK)
    #     except:
    #         return Response(data={'message': 'email does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(["POST"])
def sign_up(request):
    print(request.data)
    form = CreateUserForm(request.data)
    if form.is_valid():
        form.save()
        messages.success(request, "Acount was created successfuly")
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
    # serialized_data = signUpSerializer(data=request.data)
    # if serialized_data.is_valid(raise_exception=True):
    #     new_user = User(email=serialized_data.validated_data['email'],
    #                     password=serialized_data.validated_data['password'],
    #                     name=serialized_data.validated_data['name'],
    #                     role=serialized_data.validated_data['role'])
    #     new_user.save()
    #     return Response(data={'message': 'done'}, status=status.HTTP_200_OK)
    
@login_required(login_url='/login')
def logout_user(request):
    logout(request)
    return Response(data={'message': 'done'}, status=status.HTTP_200_OK)

@login_required(login_url='/login')
def home_page(request):
    return Response(data={'message': 'done'}, status=status.HTTP_200_OK)