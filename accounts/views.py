from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required
from accounts.forms import LoginForm, RegistrationForm, UserEditForm, ProfileEditForm
from accounts.models import Profile
import re

class LoginView(View):
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            user = authenticate(request,username = cd['username'], password = cd['passwords'])
            if user is None:
                return HttpResponse('Неправильный логин и/или пароль')
            if not user.is_active:
                return HttpResponse('Ваш аккаунт заблокирован')
            login(request,user)
            return HttpResponse('Добро пожаловать! Успешный вход')
        
        return render(request, 'accounts/login.html', {'form': form})
    
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            Profile.objects.create(user=new_user)
            
            return render(request, "accounts/registration_complete.html", {"new_user": new_user})
    else:
        form = RegistrationForm()

    return render(request, "accounts/register.html", {"reg_form": form})

@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST,files=request.FILES)
        profile_form.data._mutable = True
        profile_form.data['trello_hash'] = re.sub(r'[^a-zA-Z0-9 ]',r'',profile_form.data['trello_hash'])
        profile_form.data._mutable = False

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    
    return render(request,"accounts/edit.html",{"user_form": user_form, "profile_form": profile_form, "trello_url": 'https://trello.com/1/authorize?expiration=never&name=MyPersonalToken&scope=read&response_type=token&key=cded61b0ea3c8c0fc639dc3faee0abf8'})
