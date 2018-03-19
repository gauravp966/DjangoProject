from django.shortcuts import render
from third_app import forms
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from third_app.models import UserProfileInfo
# Create your views here.


def index(request):
    return render(request, 'third_app/index.html')


def register(request):
    register = False
    if request.method=='POST':
        user_form = forms.UserForm(request.POST)
        profile_form = forms.UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user     #for one to one relationship

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            register = True

    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileForm()
    return render(request,'third_app/register.html',{'user_form':user_form,'profile_form':profile_form,'register':register})


def user_login(request):
    if request.method == 'POST':
        login_form = forms.UserLoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request,user)
                request.session['username'] = username
                return HttpResponseRedirect(reverse('third_app:index'))
            else:
                return HttpResponse('Invalid Login Details')

    else:
        login_form = forms.UserLoginForm()
    return render(request, 'third_app/login.html', {'form':login_form})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('third_app:index'))

@login_required
def special(request):
    if request.session['username']:
        user = User.objects.get(username=request.session['username'])
        user_profile = UserProfileInfo.objects.get(user=user)
    else:
        print('login again, session expired')

    return render(request, 'third_app/special.html',{'user':user,'user_profile':user_profile})