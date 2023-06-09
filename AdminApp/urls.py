from django.urls import path

from .views import *

app_name = "adminApp" 
urlpatterns = [
    path('allcities', allcities, name='allcities'),
    path('CreateCity', CreateCity, name='CreateCity'),
    path('EditCity:<int:pk>', EditCity, name='EditCity'),
    path('DeleteCity:<int:pk>', DeleteCity, name='DeleteCity'),
    
    path('allCategories', allCategories, name='allCategories'),
    path('CreateCategory', CreateCategory, name='CreateCategory'),
    path('EditCategory:<int:pk>', EditCategory, name='EditCategory'),
    path('DeleteCategory:<int:pk>', DeleteCategory, name='DeleteCategory'),
    
    path('ProviderUsers', ProviderUsers, name='ProviderUsers'),
    path('ClientUsers', ClientUsers, name='ClientUsers'),
    
    
    path('ChangeUserStatus:<int:pk>', ChangeUserStatus, name='ChangeUserStatus'),
    path('DeleteUser:<int:pk>', DeleteUser, name='DeleteUser'),
    
    
    
    

    
    
    
]