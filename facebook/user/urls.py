from django.contrib import admin
from django.urls import path
from .views import user_registration,user_login,user_info,searching,user_info_update,logout,search_info,update_profile_pic,interface



app_name = 'user'
urlpatterns = [
    path('',interface,name='interface'),
    path('registartion/',user_registration,name='registration'),
    path('login/',user_login,name='login',),
    path('info/',user_info,name='user-info'),
    path('search/',searching,name='search'),
    path('update/',user_info_update,name='update'),
    path('logout/',logout,name='logout'),
    path('search_info/<int:pk>/',search_info,name='search-info'),
    path('update_profile_pic/',update_profile_pic,name='update-profile-pic'),
]
