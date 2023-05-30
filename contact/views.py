from django.shortcuts import render

# Create your views here.
def contactpageload(request):
    return render(request,'contactus.html')