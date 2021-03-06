"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views 
from users import views as user_views
#to access media files on browswer
from django.conf import settings
from django.conf.urls.static import static
#favicon
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.index,name="index"),
    path('register/', user_views.register, name='register'),
    path('home/',user_views.home,name='home'),
    path('profile/', user_views.profile, name='profile'),
    path('oauth/', include('social_django.urls', namespace='social')), 
    path('profile_settings/', user_views.profile_settings, name='profile_settings'),
    path('settings/password', user_views.password, name='password'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', 
        auth_views.PasswordResetView.as_view(
            template_name='users/password_reset.html'
        ),
        name='password_reset'),
    path('password-reset/confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html'
        ),
        name='password_reset_confirm'),
    path('password-reset/done/', 
        auth_views.PasswordResetDoneView.as_view(
            template_name='users/password_reset_done.html'
        ),
        name='password_reset_done'),
    path('password-reset-complete/', 
        auth_views.PasswordResetCompleteView.as_view(
            template_name='users/password_reset_complete.html'
        ),
        name='password_reset_complete'),
    path('password-change/', 
        auth_views.PasswordChangeView.as_view(
            template_name='users/password_change.html'
        ),
        name='password_change'),
    path('password-change-done/', 
        auth_views.PasswordChangeDoneView.as_view(
            template_name='users/password_change_done.html'
        ),
        name='password_change_done'),
    path('delete-user',user_views.delete_user_profile,name='delete_user'),
    path('corporate/', include('employer.urls')),
    path('select2/', include('django_select2.urls')),#select2
    path('about/',user_views.about,name='about'),
    path('contact/',user_views.contact,name='contact'),
    path('chat/',user_views.chat,name='chat'),
    path('favicon.ico',RedirectView.as_view(url='/media/favicon.ico')),#favicon
    
]
#to access media files on browswer
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)