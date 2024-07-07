from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Mechanic

def find_nearby_mechanics(user_location):
    radius = 10000  # 10 kilometers in meters
    user_point = Point(user_location[1], user_location[0], srid=4326)
    nearby_mechanics = Mechanic.objects.annotate(
        distance=Distance('geo_location', user_point)
    ).filter(distance__lte=radius).order_by('distance')
    return nearby_mechanics

