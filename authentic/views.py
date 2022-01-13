from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.views.generic import  View
from django.http import HttpResponse
from authentic.forms import UserForm
from django.urls import reverse_lazy
from django.contrib.auth import  authenticate,login,logout,password_validation

from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView,PasswordChangeView,PasswordChangeDoneView

from user.models import User
# Create your views here.
def home(request):
    return HttpResponse("hekk")


class  signup_view(View):
    template_name ='authentication/signup.html'
    form_class = UserForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('feed/')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin_view')

        context = {'form':form}
        return render(request, self.template_name,context)




class  signin_view(View):
    template_name ='authentication/signin.html'

    def get(self, request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('feed/')
        return render(request,self.template_name)
    def post(self, request,*args,**kwargs):
        email_username = request.POST.get('email_username')
        password = request.POST.get('password')
        try:
            user_obj =   User.objects.get(username =email_username)
            email = user_obj.email
        except Exception as e:
            email = email_username
               
        user= authenticate(request,email=email,password=password)
        if user is None:
            return render(request, self.template_name,context={'messages':'Invalid Login'})
        else:
            login(request , user)
            return redirect('feed/')
        return render(request,self.template_name)

class  home_feed(View):
    def get(self, request,*args,**kwargs):
        return HttpResponse("hekki")
    

class SignOutView(View):
    def post(self, request,*args,**kwargs):
        logout(request)
        return redirect('signin_view')


class PRView(PasswordResetView):
    email_template_name = 'authentication/password_reset_email.html'
    template_name = 'authentication/password_reset.html'

class PRDone(PasswordResetDoneView):
    template_name = 'authentication/password_reset_done.html'

class PRConfirm(PasswordResetConfirmView):
    template_name = 'authentication/password_reset_confirm.html'

class PRComplete(PasswordResetCompleteView):
    template_name = 'authentication/password_reset_complete.html'


class PWDChangeView(PasswordChangeView):
    template_name = 'authentication/password_change.html'
    success_url = reverse_lazy('password_change_done_view')

class PWDChangeDoneView(PasswordChangeDoneView):
    template_name = 'authentication/password_change_done.html'