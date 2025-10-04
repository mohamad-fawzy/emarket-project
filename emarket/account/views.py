from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer
from .services import generate_token




@api_view(['POST'])
def register_user(request):
    serializers = UserSerializer(data = request.data)
    if serializers.is_valid():
        serializers.save()
        tokens = generate_token(
        username=serializers.instance.username,
        password=request.data.get("password")
        )
        return Response({"user": serializers.data, "tokens": tokens},status=status.HTTP_201_CREATED)
    else: return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    login_user=generate_token(username , password)
    return Response(login_user , status=status.HTTP_200_OK)





    



@api_view(['PUT'])
def update_user(request):
    user = request.user
    serializers = UserSerializer(user, data = request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    else: return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def delete_user(request):
    user = request.user
    serializers = UserSerializer(user)
    serializers.delete()
    return Response({'mess':'user is deleted' }, status=status.HTTP_201_CREATED)






























