from django.shortcuts import render
from mymodels.models import Request

# Create your views here.
def dashboard(request):
    myrequests = Request.objects.filter(id=1)

    return render(request,"mechanic/dashboard.html",{myrequests:myrequests})

