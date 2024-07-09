from django.shortcuts import render
from .forms import RequestForm
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D

def place_request(request):
    mechanics = []
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            request_instance = form.save(commit=False)
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')
            request_instance.geo_location = Point(float(longitude), float(latitude), srid=4326)
            request_instance.save()      

    else:
        form = RequestForm()

    return render(request, 'request.html', {'form': form, 'mechanics': mechanics})
