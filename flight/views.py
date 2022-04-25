from django.shortcuts import render
from .models import *
from .serializers import *
from django.http import JsonResponse


# Create your views here.
def flights(request):
    all_flights = Flight.object.all()
    flights_serializer = FlightSerializer(all_flights, many=True)
    return JsonResponse(flights_serializer, safe=False)



