from django.shortcuts import render
from django.utils.translation import get_language, activate, gettext as _

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse, Http404
from django.db.models import Q
from AdminApp.models import *
from .forms import *
from .models import *
import datetime
from AdminApp.forms import *

def signIn(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(request, username=username,
                                password=raw_password)
            # and not user.is_superuser
            if user is not None :
                login(request,user)
                # messages.success(request, 'successfully login')
                return redirect('dashboard')
            else:
                # messages.error(
                    # request, 'Please enter correct username and password combination')
                return redirect('/')
    else:
        form = SignInForm()
    return render(request, 'users/login.html', {'form': form})

def dashboard(request):
    # , {'form': form}
    provider_users = User.objects.filter(user_role = 'Provider').count()
    client_users = User.objects.filter(user_role = 'Client').count()
    # all_users = User.objects.filter(
    #                 Q(user_role = 'Provider') | 
    #                 Q(user_role = 'Client') 
    #             ).count()
    admin_users = User.objects.filter(is_superuser=True).count()
                # User.objects.filter(
                #     Q(user_role = 'Provider')| 
                #     Q(user_role = 'Client') 
                # ).exclude(
                #     user_role=False
                # ).count()
    all_users = provider_users + client_users
    context = {
        'provider_users' : provider_users,
        'client_users' : client_users,
        'admin_users' : admin_users,
        'all_users' : all_users
    }
    
    return render(request, 'users/dashboard.html', context)


def home(request):
    # trans = _('hello')
    trans = translate(language='fr')
    return render(request, 'users/home.html', {'trans': trans})

def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = _('hello')
    finally:
        activate(cur_language)
    return text


def index(request):
    form = SignUpForm(request.POST or None, request.FILES or None)
    categories = Category.objects.all()
    cities = City.objects.all()
    services = Service.objects.all()
    
    
    provider_users = User.objects.filter(user_role = 'Provider').count()
    client_users = User.objects.filter(user_role = 'Client').count()
    form2 = SignInForm()
    context = {
        "form": form,
        "categories" : categories,
        "categories_count": categories.count(),
        "services_count": services.count(),
        
        "provider_users": provider_users,
        "client_users": client_users,
        "cities" : cities,
        "form2": form2
        
        
    }
    if request.method == 'POST':
        print(form)
        if form.is_valid():
            form.save()
            context['noerrors']= True
            context['signedup']= True
            
            
        else:
            print('i am in errors')
            print(form.errors)
            context['errors']= True
        
    
    return render(request, 'finder/index-2.html',context)


def all_categories(request):
    categories = Category.objects.all()
    form = SignUpForm(request.POST or None, request.FILES or None)
    form2 = SignInForm()

    context = {
        "categories" : categories,
        "categories_count": categories.count(),
        "form": form,
        "form2": form2
        
        
    }
    return render(request, 'finder/all-categories.html',context)



def mcdashboard(request):
    return render(request, 'finder/mc-dashboard.html')


def categories_details(request, pk):
    category = Category.objects.get(id=pk)
    
    form = SignUpForm(request.POST or None, request.FILES or None)
    form2 = SignInForm()

    
    categories = Category.objects.all()
    cities = City.objects.all()
    
    context = {
        "category" : category,
        "form": form,
        "categories" : categories,
        "cities" : cities,
        "form2": form2
        
        # "categories_count": categories.count(),
        
    }
    # return render(request, 'finder/categorydetail.html',context)
    
    return render(request, 'finder/categories-detail-2.html',context)



import os
from twilio.rest import Client
account_sid = 'AC5952a5390463316c063d921232801a55'
auth_token = 'dcd39a69f82c2cb1376bd353dcc9ca0c'
client = Client(account_sid, auth_token)



def twilliomsg(request):
    
    message = client.messages.create(
                        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                        from_='+16692051337',

                        #  to='+15558675310'
                        to='+212623446847'
                        
                )
    print(message.sid)
    
    
    return render(request, 'finder/mc-dashboard.html')


def register(request):
    return render(request, 'finder/mc-dashboard.html')


def log_in(request):
    if request.method == 'POST':
        form2 = SignInForm(request.POST)
        if form2.is_valid():
            username = form2.cleaned_data.get('username')
            raw_password = form2.cleaned_data.get('password')
            user = authenticate(request, username=username,
                                password=raw_password)
            # and not user.is_superuser
            if user is not None and not user.is_superuser :
                login(request,user)

                if user.user_role == 'Provider':
                    return redirect('Providerdashboard')
                    
                elif user.user_role == 'Client':
                    
                # messages.success(request, 'successfully login')
                    return redirect('Clientdashboard')
            else:
                # messages.error(
                    # request, 'Please enter correct username and password combination')
                return redirect('index')
    # else:
        # form2 = SignInForm()
    # return render(request, 'users/login.html', {'form2': form2})

def Providerdashboard(request):
    
    provider_user = User.objects.get(id=request.user.id)
    cities = City.objects.all()
    
    form = SignUpForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        address = request.POST.get('address')
        
        provider_user.first_name = first_name
        provider_user.last_name = last_name
        provider_user.gender = gender
        db_city = City.objects.get(id=city)
        
        provider_user.city = db_city
        provider_user.address = address
        provider_user.save()
        
        
    context = {
        "provider_user" : provider_user,
        "cities": cities,
        "form": form,
        # "myform": myform
        
    }
    return render(request, 'finder/Providerdashboard.html',context)
    # return render(request, 'baseProvider.html')
    
def ProviderService(request):
    my_service = Service.objects.filter(provider_user=request.user.id)
    context = {}
    if my_service:
        my_service = my_service[0]
        
        context["my_service"] = my_service
        context["user"] = request.user
        
    
    return render(request, 'finder/services.html', context)

def delete_service(request,id):
    c=Service.objects.filter(id=id).delete()
    # messages.success(request, 'Kmi file has been Successfully Deleted')
    return redirect('ProviderService')


    
    
    
@login_required
def EditService(request, id):
    context={}
    # obj= get_object_or_404(User, username=id)
    service_obj = Service.objects.get(id=id)
    service_images = ServiceImage.objects.filter(service=service_obj)
    # provide_user = User.objects.get(id=request.user.id)
    
    form = ServiceForm(request.POST or None, request.FILES or None, instance=service_obj )
    # form = updatePasswordForm(request.POST or None, instance= obj)
    # context ['form']= form
    # context ['users']= obj.username
    # context ['name']= str(obj.first_name) +' '+ str(obj.last_name)

    # form = updateTeacherForm(instance=obj)
    # myform = updateTeachermodelForm(instance=obj.teachermodel)
    # passform = updatePasswordForm(request.POST or None, instance=obj)
    
    context = {
        'form': form,
        'service_obj' : service_obj,
        'service_images': service_images
    }
    services_images = request.FILES.getlist('services_images',None)
    if services_images:
        ServiceImage.objects.filter(
                    service = service_obj
                ).delete()
        try:
            for img in services_images:
                ServiceImage.objects.create(
                    image = img,
                    service = service_obj
                )
        except Exception as e :
            print(e)
    print(services_images)
    print(services_images)    
    print(services_images)    
    print(services_images)    
    print(services_images)    
    print(services_images)    
    print(services_images)    
        
    if form.is_valid():
        form.instance.provider_user = request.user
        obj = form.save()
        # context['passwordchanged'] = True
    # else:
        # context['passwordnotchanged'] = True
    return render(request, 'finder/editservice.html',context)


def CreateService(request):
    
    # request.POST, request.FILES or None   ,provider_user=request.user.id
    form = ServiceForm(request.POST or None, request.FILES or None )
    # }
    context = {
        "form" : form,
    }
    service_created = False
    is_provided_user = False
    len_images = False
    
    if request.method == 'POST':
        provide_user = User.objects.get(id=request.user.id)
        services_images = request.FILES.getlist('services_images')
        if len(services_images) < 4:
            if form.is_valid():
                if not Service.objects.filter(provider_user=request.user.id).exists():
                    
                    form.instance.provider_user = provide_user
                    
                    service = form.save()
                    print(service)
                    
                    try:
                    
                        for img in services_images:
                            ServiceImage.objects.create(
                                image = img,
                                service = service
                            )
                    except Exception as e :
                        print(e)
                    service_created = True
                    count=0
                    try:
                        pass
                    except Exception as e :
                        pass
                    return redirect('ProviderService')
                    
                else:
                    is_provided_user = True
                    
            else:
                print(form.errors)
            
                
    context['len_images'] = len_images
    context['service_created'] = service_created
    context['is_provided_user'] = is_provided_user            
                
    return render(request, 'finder/createservice.html',context)
