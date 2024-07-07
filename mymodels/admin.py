from django.contrib import admin
from .models import User, Mechanic, Car, Service, Request, Availability

admin.site.register(User)
admin.site.register(Mechanic)
admin.site.register(Car)
admin.site.register(Service)
admin.site.register(Request)
admin.site.register(Availability)

