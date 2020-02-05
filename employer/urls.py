##from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views 
from . import views
#to access media files on browswer
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    RequestDetailView,
    RequestDeleteView,
    RequestUpdateView
)
urlpatterns = [
    path('', views.index,name="c-index"),
    path('home/', views.home,name="c-home"),
    path('register/', views.register,name="c-register"),
    path('request/<int:pk>/', RequestDetailView.as_view(), name='request-detail'),
    path('request/<int:pk>/update/', RequestUpdateView.as_view(), name='request-update'),
    path('request/<int:pk>/delete/', RequestDeleteView.as_view(), name='request-delete'),
    
    
]
#to access media files on browswer
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)