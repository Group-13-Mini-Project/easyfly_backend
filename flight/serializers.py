from rest_framework import serializers
from .models import *


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ["id", 'source', 'destination', 'airplane', 'cost',
                  'flight_type', 'flight_class',
                  "duration", 'departure_date',
                  "return_date"
                  ]
