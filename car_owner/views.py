from django.shortcuts import render,get_object_or_404,redirect
from .forms import RequestForm
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from mymodels.models import Mechanic,Custom_User,Notification
from django.contrib import messages

def place_request(request, mec):
    mechanic_id = int(mec)
    mechanic = get_object_or_404(Custom_User, id=mechanic_id)
    mechanics = [mechanic]  # Add the selected mechanic to the list

    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            request_instance = form.save(commit=False)
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')
            if latitude and longitude:
                request_instance.geo_location = Point(float(longitude), float(latitude), srid=4326)
            request_instance.user = mechanic  # mechanic requested for service
            request_instance.save()
            # Optionally, you can redirect to a success page or the request detail page
            # messages.success(request, 'Request has been sent')
            email = request.POST.get('email')
            car_number = request.POST.get('car_number')

            notification = Notification(
                user = mechanic,
                message = f"New request: {email} from {car_number}"
            )
            notification.save()
            return redirect('/')
        
        
        print(f"request.POST type: {type(request.POST)}")
        print(f"latitude: {latitude}, longitude: {longitude}")
        print(f"form.is_valid(): {form.is_valid()}")


    else:
        form = RequestForm()

    return render(request, 'car_owner/make_request.html', {'form': form, 'mechanics': mechanics})