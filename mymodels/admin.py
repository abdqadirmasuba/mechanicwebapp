from django.contrib import admin
from .models import User, Mechanic, Service, Request, Availability

admin.site.register(User)
admin.site.register(Mechanic)
admin.site.register(Service)
admin.site.register(Request)
admin.site.register(Availability)

