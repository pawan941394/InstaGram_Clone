from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import View
from django.contrib.auth import get_user_model
from user.forms import UserEditForm
from django.db.models import Q
from django.contrib import messages
User = get_user_model()
# Create your views here.
class ProfileView(View):
    template_auth = 'user/authenticated_profile.html'
    template_ano = 'user/anonymous_profile.html'
    def get(self,request,*args,**kwargs):
        username = kwargs.get('username')

        try:
            user = User.objects.get(username=username)
        except Exception as e:
            return HttpResponse('<h1>This page doesnot exit</h1>')

        if username == request.user.username:
    
            context = {'user':user}
            return render(request,self.template_auth,context)
        else:
            is_follows_this_user = False
            for follower_user in request.user.follow_follower.all():
                if user == follower_user.followed:
                    is_follows_this_user = True
            context = {'user':user,'is_follows_this_user':is_follows_this_user}
            return render(request,self.template_ano,context)
class ProfileEditView(View):
    template_name = 'user/profile_edit.html'
    formclass = UserEditForm
    def get(self,request,*args,**kwargs):
        username = kwargs.get('username')
        if username != request.user.username:
            return HttpResponse("This page doesn't exit")
        form = self.formclass(instance =request.user)
        context = {'form':form}
        return render(request,self.template_name,context)
    def post(self,request,*args,**kwargs):
        form = self.formclass(request.POST,request.FILES,instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request,'Saved your details in safe place')
            return redirect('profile_edit_view',request.user.username)

        else:
            for field in form.errors:
                form[field].field.widget.attrs['class']+= ' is-invalid'
            messages.error(request,'Something went wrong please check again')
            return render(request,self.template_name,{'form':form})



class AllProfileViews(View):
    template_name = 'user/all_profiles.html'
    def get(self,request,*args, **kwargs):
        search_term = request.GET.get('query')
        if search_term:
            all_profiles = User.objects.filter(Q(username__contains=search_term) | Q(full_name__contains = search_term )).exclude(username=request.user.username)
        else :
            all_profiles = User.objects.none()
        context  = {'all_profiles':all_profiles}
        return render(request,self.template_name,context=context)

