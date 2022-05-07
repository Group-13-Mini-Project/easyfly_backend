from rest_framework import serializers
from .models import *


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ["id", 'source', 'destination', 'airplane', 'cost',
                  'flight_type', 'flight_class',
                  "duration", "destination"
                  "return_date"
                  ]


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = [
            "city_name", "city_code"
        ]