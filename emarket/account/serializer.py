from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password





class Sinupserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password') 

    extra_kwargs = {
        'first_name': {'required':True , 'allow_blank':False},
        'last_name' : {'required':True , 'allow_blank':False},
        'email': {'required':True , 'allow_blank':False},
        'password': {'required':True , 'allow_blank':False, 'min_length':8 },
        
    }  

    def create(self, validated_data):
        user = User.objects.create(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            username = validated_data['email'],  
            password = make_password(validated_data['password'])
        )
        return user



class Userserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password') 

    