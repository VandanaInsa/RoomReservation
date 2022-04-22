from datetime import timedelta, datetime


from django.shortcuts import render
from . models import Room, Reservation

# Create your views here.
def home(request):
    return render(request,'app/home.html')



