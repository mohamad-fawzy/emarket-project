from rest_framework import serializers
from django.contrib.auth.models import User
from .validators import UniqData




class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = fields = ('id','first_name', 'last_name', 'email', 'password', 'is_active')
        extra_kwargs = {
        'first_name': {'required':True , 'allow_blank':False},
        'last_name' : {'required':True , 'allow_blank':False},
        'email': {'required':True ,'validators': [UniqData]},
        'password': {'required':True ,'write_only': True, 'allow_blank':False, 'min_length':8 },
        'is_active': {'default': True}

    }  
        
    def create(self, validated_data):
        user = User.objects.create(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            username = validated_data['email'],  
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.email = validated_data.get("email", instance.email)
        instance.username = validated_data.get("email", instance.username)
        password = validated_data.get("password", None)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


# User Data
class UserDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }


        
        







    