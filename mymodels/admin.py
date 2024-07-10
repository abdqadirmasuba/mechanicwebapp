from django.contrib import admin
from .models import Custom_User, Mechanic, Service, Request, Availability

admin.site.register(Custom_User)
admin.site.register(Mechanic)
admin.site.register(Service)
admin.site.register(Request)
admin.site.register(Availability)

