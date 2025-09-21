from rest_framework import serializers
from .models import Product
from .models import Category
class ProductSerializers(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    def validate_name(self, value):
        if Category.objects.filter(name=value).exists():
            raise serializers.ValidationError("هذا الصنف موجود بالفعل.")
        return value
    class Meta:
        model = Product
        fields = '__all__'
