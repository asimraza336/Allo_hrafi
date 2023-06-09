from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *


urlpatterns = [
    path('signin', signIn, name='signIn'),

    
    path('home', home, name="home"),
    path('dashboard', dashboard, name='dashboard'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    
    path('', index, name='index'),
    path('all-categories', all_categories, name='all_categories'),
    path('categories-details:<int:pk>', categories_details, name='categories_details'),
    
    path('mcdashboard', mcdashboard, name='mcdashboard'),
    
    path('twilliomsg', twilliomsg, name='twilliomsg'),
    
    path('register', register, name='register'),
    path('log-in', log_in, name='log-in'),
    path('Providerdashboard', Providerdashboard, name='Providerdashboard'),
    path('Service', ProviderService, name='ProviderService'),
    path('CreateService', CreateService, name='CreateService'),
    path('delete_service/<int:id>', delete_service, name='delete_service'),
    path('EditService/<int:id>', EditService, name='EditService'),
    
    
    
    
    
    
    
    
]