from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProductSerializers
from .filters import ProductFilter

from .models import Product

# Create your views here.

@api_view(['GET'])
def get_all_products(request): 
    # get_products = Product.objects.all()
    filter_set = ProductFilter(request.GET, queryset=Product.objects.all().order_by('id') )
    serializers = ProductSerializers(filter_set.qs, many=True)
    print('api done')
    return Response({"products_res": serializers.data})



@api_view(['GET'])
def get_products_py_id(request, pk): 
    get_one_products = get_object_or_404(Product , id=pk)
    serializers = ProductSerializers(get_one_products, many=False)
    print('api done one pro')
    return Response({"one_product_res": serializers.data})

