import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MechanicRegistrationForm
from .models import Mechanic
from django.contrib.gis.geos import Point
from django.shortcuts import render, redirect
from .models import Mechanic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from django.core.serializers import serialize
from django.http import JsonResponse
from django.contrib.gis.geos import fromstr
from mechanic.forms import CustomUserChangeForm


# Create your views here.

def home(request):
    all_mechanics = Mechanic.objects.all()
    all_mechanics_json = json.loads(serialize('geojson', all_mechanics))

    return render(request, 'mymodels/home.html', {
        'all_mechanics': all_mechanics,
        'all_mechanics_json': all_mechanics_json,
    })

def get_nearby_mechanics(request):
    lat = request.GET.get('lat')
    lng = request.GET.get('lng')

    if lat and lng:
        user_location = fromstr(f'POINT({lng} {lat})', srid=4326)
        nearby_mechanics = Mechanic.objects.annotate(distance=Distance('geo_location', user_location)).filter(distance__lte=D(km=10)).order_by('distance')
        nearby_mechanics_json = json.loads(serialize('geojson', nearby_mechanics))
        return JsonResponse(nearby_mechanics_json, safe=False)
    return JsonResponse({'error': 'Invalid location'}, status=400)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('mechanic:dashboard')
        else:
            messages.error(request, 'password or user name is wrong')
            return redirect('mymodels:login_view')
             
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
            return redirect('mechanic:dashboard')
   
    else:
        form = MechanicRegistrationForm()
    return render(request, 'mymodels/register.html', {'reg_form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('mymodels:login_view')