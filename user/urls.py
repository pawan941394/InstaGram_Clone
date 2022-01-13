
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from core.views import HomeView
from django.urls import include, re_path
from .import views
from user.views import ProfileView,ProfileEditView,AllProfileViews
from django.contrib.auth.decorators import  login_required
urlpatterns = [
     path('in/<str:username>/',  login_required(ProfileView.as_view()) , name= 'profile_view'),
     path('in/<str:username>/edit/',  login_required(ProfileEditView.as_view()) , name= 'profile_edit_view'),
    
     path('profiles/',  login_required(AllProfileViews.as_view()) , name= 'all_profiles_view'),
    
]
