from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from django.http import JsonResponse


# Create your views here.
@api_view(['GET',])
@permission_classes((IsAuthenticated, ))
def flights(request):
    all_flights = Flight.objects.all()
    flights_serializer = FlightSerializer(all_flights, many=True)
    return JsonResponse(flights_serializer.data, safe=False)



