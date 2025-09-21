from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializer import Sinupserializers
from .serializer import Userserializers




@api_view(['POST' , 'GET'])
def register_andGet(request):
# Get current authenticated user data
    if request.method =='GET':
        user = request.user
        serializer = Userserializers(user)
        return Response(serializer.data)
    
    elif request.method =='POST':    
        serializers = Sinupserializers(data = request.data)
        if serializers.is_valid():
            if not User.objects.filter(username = request.data['email']):
                serializers.save()
                return Response({'message':'Your account has been created successfully'},
                                status=status.HTTP_201_CREATED)
            else: return Response({"error": "Registration failed. This email is already in use."},
                                status=status.HTTP_400_BAD_REQUEST)
        else: return Response(serializers.errors)



@api_view(['GET'])
def get_allUsers(request):
    users = User.objects.all()
    serializer = Userserializers(users , many=True)
    return Response({'users':serializer.data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request):
    user = Sinupserializers(request.user)
    return Response(user.data)



# @api_view(['POST'])
# def register(request):
#     data = request.data
#     user = Sinupserializers(data = data)

#     if user.is_valid():
#         if not User.objects.filter(username=data['email']).exists():
#             user = User.objects.create(
#                 username = data['email'],
#                 first_name = data['first_name'],
#                 last_name = data['last_name'],
#                 email = data['email'],
#                 password = data['email'],
#             )
#             return Response({'message':'Your account has been created successfully'},
#                              status=status.HTTP_201_CREATED)
            
#         else: return Response({"error": "Registration failed. This email is already in use."},
#                                status=status.HTTP_400_BAD_REQUEST)
#     else: return Response(user.errors)