from django.urls import path
from . import views



urlpatterns = [
    path('products/', views.get_add_products, name='products' ),
    path('products/<str:pk>/', views.get_products_py_id, name='products_py_id' ),

]
