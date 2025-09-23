from django.urls import path
from . import views



urlpatterns = [
    path('register/', views.register_user, name='register' ),
    path('update/', views.update_user, name='register' ),
    path('delete/', views.delete_user, name='register' ),

    # path('all/', views.get_allUsers, name='register' ),
    # path('info_user/', views.user_info, name='userinfo' ),


]
