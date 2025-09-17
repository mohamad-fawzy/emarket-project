from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import ProductSerializers
from .filters import ProductFilter
from .models import Product

# Create your views here.

@api_view(['GET' , 'POST'])
def get_all_products(request): 
    queryset=Product.objects.all().order_by('id')

    if request.method =='GET':
            filter_set = ProductFilter(request.GET, queryset )
            serializer = ProductSerializers(filter_set.qs, many=True)
            return Response({"products_res": serializer.data})
    
    
    elif request.method =='POST':
         serializer = ProductSerializers(data = request.data)

         if Product.objects.filter(name=request.data.get('name')).exists():
            return Response(
                {"error": "Product with this name already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)




@api_view(['GET','PUT','DELETE'])
def get_products_py_id(request, pk): 
    try:
        product = Product.objects.get(pk = pk )
    except Product.DoesNotExist : return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ProductSerializers(product)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = ProductSerializers(product, data = request.data)

        if Product.objects.filter(name=request.data.get('name')).exists():
            return Response(
                {"error": "Product with this name already exists"},
                status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        product = Product.objects.get(pk = pk )
        product.delete()
        return Response({"DELETE": "PRODUCT IS DELETED" ,},
                status=status.HTTP_200_OK)


            




