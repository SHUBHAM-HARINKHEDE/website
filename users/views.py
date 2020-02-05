from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import (UserRegisterForm ,
                    UserUpdateForm, 
                    ProfileUpdateForm,
                    EducationAddForm
)
from django.contrib.auth.decorators import login_required
#to check password
from django.contrib.auth.hashers import check_password
#social Auth
from social_django.models import UserSocialAuth
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
#
from .models import Education 

# Create your views here.
def index(request):
    return render(request,'users/index.html')

def home(request):
    return render(request,'users/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account hs been created! You can login now')
            return redirect('login')
    else:
        form = UserRegisterForm(initial={'email':request.GET.get('email')})
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    #not working.....
    if request.method == 'GET':
        e_form=EducationAddForm(request.GET,instance=request.user)
        if e_form.is_valid():
            e_form.save()
            messages.success(request, f'College({e_form}) has been added!')
            return redirect('profile')
     #...........       
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES, 
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Profile has been Updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        e_form =EducationAddForm()
        edu=Education.objects.filter(user=request.user)

    context = {
        'u_form' : u_form,
        'p_form' : p_form,
        'e_form' : e_form,
        'edu'    : edu   
       }
    return render(request, 'users/profile.html',context)

@login_required
def profile_settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'users/profile_settings.html', {
        'github_login': github_login,
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
        #return render(request, 'password-change')
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'users/password.html', {'form': form})

@login_required
def delete_user_profile(request):
    if request.method == 'POST':
        if check_password(request.POST.get('password'),request.user.password):   
            request.user.delete()
            return render(request,'users/delete_profile_done.html')
        else:
            messages.error(request,"Please enter correct password to procced!",)
    return render(request,'users/delete_profile.html')
