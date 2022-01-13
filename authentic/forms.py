from django import  forms
from user.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('full_name','email','username','password1','password2')

        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('full_name','email','username')

        
