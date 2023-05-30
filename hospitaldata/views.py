from django.shortcuts import render
from .models import Staff
# Create your views here.
def staffpageload(request):
    doctors = Staff.objects.all()
    context = {'doctors':doctors}
    return render(request,"doctors-staff.html",context)

def departmentspageload(request):
    return render(request,"departments.html")