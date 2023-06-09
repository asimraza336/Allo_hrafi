from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse, Http404
from django.db.models import Q
from django.contrib import messages
from Users.models import User
from .models import *
from .forms import *


def allcities(request):
    cities = City.objects.all()
    context = {
        "cities" : cities
    }
    return render(request, 'admintemp/allcities.html', context)


def CreateCity(request):
    form = CityForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully City has been Added...!!!')
        return redirect('adminApp:allcities')
    context={
        'form': form
    }
    return render(request, 'admintemp/create_city.html',context)
    
    
def EditCity(request, pk):
    specific_city = City.objects.get(id=pk)
    
    form = CityForm(request.POST or None, instance= specific_city)
    if form.is_valid():
        form.save()
        messages.success(request, 'Updated City ...!!!')
        return redirect('adminApp:allcities')
    context={
        'form': form
    }
    return render(request, 'admintemp/create_city.html',context)


def DeleteCity(request, pk):

    city_deleted = City.objects.filter(id=pk).delete()
    messages.error(request, 'City has been Successfully Deleted')
    return redirect('adminApp:allcities')


def allCategories(request):
    categories = Category.objects.all()
    context = {
        "categories" : categories
    }
    return render(request, 'admintemp/all_categories.html', context)


def CreateCategory(request):
    form = CategoryForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Categiory has been Added...!!!')
        return redirect('adminApp:allCategories')
    context={
        'form': form
    }
    return render(request, 'admintemp/create_category.html',context)


def EditCategory(request, pk):
    specific_category = Category.objects.get(id=pk)
    print(specific_category)
    form = CategoryForm(request.POST or None, request.FILES or None, instance= specific_category)
    if form.is_valid():
        form.save()
        messages.success(request, 'Updated Category ...!!!')
        return redirect('adminApp:allCategories')
    context={
        'form': form
    }
    return render(request, 'admintemp/edit_category.html',context)


def DeleteCategory(request, pk):

    category_deleted = Category.objects.filter(id=pk).delete()
    messages.error(request, 'Category has been Successfully Deleted')
    return redirect('adminApp:allCategories')


def ProviderUsers(request):
    
    provider_user = User.objects.filter(user_role='Provider')
    # provider_user = User.objects.all()
    print(provider_user)
    context = {
        "provider_user" : provider_user
    }
    return render(request, 'users/providerusers.html', context)



def ClientUsers(request):
    
    client_user = User.objects.filter(user_role='Client')
    # client_user = User.objects.all()
    print(client_user)
    context = {
        "client_user" : client_user
    }
    return render(request, 'users/clientusers.html', context)


def ChangeUserStatus(request, pk):
    try:
        user_profile = User.objects.get(id=pk)
        if user_profile.is_active:
            user_profile.is_active = False
        else:
            user_profile.is_active = True
        user_profile.save()
    except Exception as e:
        pass
    messages.success(request, 'User status has been Successfully changed...!')
    
    if user_profile.user_role == 'Provider':
        return redirect('adminApp:ProviderUsers')
    elif user_profile.user_role == 'Client':
        return redirect('adminApp:ClientUsers')
    
def DeleteUser(request, pk):

    delete_user = User.objects.filter(id=pk)
    user_role = delete_user[0].user_role 
    delete_user.delete()
    messages.error(request, 'User has been Successfully Deleted')
    if user_role == 'Provider':
        return redirect('adminApp:ProviderUsers')
    elif user_role == 'Client':
        return redirect('adminApp:ClientUsers')
    
    
