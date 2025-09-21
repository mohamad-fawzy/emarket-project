from django.urls import path
from . import views



urlpatterns = [
    path('register_andGet/', views.register_andGet, name='register' ),
    path('all/', views.get_allUsers, name='register' ),
    path('userInfo/', views.user_info, name='userinfo' ),


]
