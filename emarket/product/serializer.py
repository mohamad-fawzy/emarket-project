from rest_framework import serializers
from .models import Product

class ProductSerializers(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('name', 'description', 'price')
