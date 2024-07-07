from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MechanicRegistrationForm
from .models import Mechanic
from django.contrib.gis.geos import Point

# Create your views here.

def home(request):
    return render(request,"mymodels/home.html")

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('mechanic:dashboard')
        else:
            messages.error(request, 'password or user name is wrong')
            return redirect('general:login')
             
    return render(request,"mymodels/login.html")

def register(request):
    if request.method == 'POST':
        form = MechanicRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')
            geo_location = Point(float(longitude), float(latitude), srid=4326)
            Mechanic.objects.create(
                user=user,
                experience=form.cleaned_data['experience'],
                vehicles_of_expertise=form.cleaned_data['vehicles_of_expertise'],
                location=form.cleaned_data['location'],
                work_hours=form.cleaned_data['work_hours'],
                geo_location=geo_location
            )
            login(request, user)
            print("sent in ")
            return redirect('mechanic:dashboard')
   
    else:
        form = MechanicRegistrationForm()
    return render(request, 'mymodels/register.html', {'reg_form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('mechanic:dashboard')