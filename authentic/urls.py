
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from authentic.views import  signup_view,signin_view,home_feed,SignOutView,   PRView, PRDone, PRConfirm, PRComplete,PWDChangeView, PWDChangeDoneView
from django.urls import include, re_path

from django.urls import reverse_lazy
from .import views
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordChangeDoneView,
    )

urlpatterns = [
     path('signup/',  signup_view.as_view() , name= 'signup_view'),
     path('',  signin_view.as_view() , name= 'signin_view'),
     path('signout/',  SignOutView.as_view() , name= 'signout_view'),
     path('feed/', include('core.urls')),
      path('password/reset/', 
        PasswordResetView.as_view(
            email_template_name = 'authentication/password_reset_email.html',
            template_name = 'authentication/password_reset.html',
        ), 
        name='password_reset'),
    
    path('password/reset/done/',  
        PasswordResetDoneView.as_view(
            template_name = 'authentication/password_reset_done.html'
        ) ,
        name='password_reset_done'),

    path('password/reset/confirm/<uidb64>/<token>', 
        PasswordResetConfirmView.as_view(
            template_name = 'authentication/password_reset_confirm.html'
        ) , 
        name='password_reset_confirm'),

    path('password/reset/complete/', 
        PasswordResetCompleteView.as_view(
            template_name = 'authentication/password_reset_complete.html'
        ) , 
        name='password_reset_complete'),


    path(
        'password/change/', 
        PasswordChangeView.as_view(
            template_name = 'authentication/password_change.html',
            success_url = reverse_lazy('password_change_done_view')
            ), 
        name='password_change_view'
        ),
    path(
        'password/change/done/', 
        PasswordResetDoneView.as_view(
            template_name = 'authentication/password_change_done.html'
            ), 
        name='password_change_done_view'
        )
]
