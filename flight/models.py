from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    country_name = models.CharField(max_length=100)
    city_code = models.CharField(max_length=5)
    city_name = models.CharField(max_length=100)


class Airport(models.Model):
    name = models.CharField(max_length=100)
    city_code = models.ForeignKey(City, on_delete=models.RESTRICT)
    terminal = models.CharField(max_length=50)
    gate = models.CharField(max_length=50)


class Airplane(models.Model):
    name = models.CharField(max_length=50)
    number_of_seats = models.IntegerField()


class Flight(models.Model):
    FLIGHT_TYPES = [('OW', 'One Way'), ('RT', 'Round Trip')]
    FLIGHT_CLASS = [('FC', 'First Class'), ('BC', 'Business Class'), ('E', 'Economy')]
    airplane = models.ForeignKey(Airplane, on_delete=models.RESTRICT, related_name="flights")
    source = models.ForeignKey(Airport, on_delete=models.RESTRICT, related_name="moving_flights")
    destination = models.ForeignKey(Airport, on_delete=models.RESTRICT, related_name="arriving_flights")
    duration = models.IntegerField()
    flight_type = models.CharField(max_length=2, choices=FLIGHT_TYPES)
    flight_class = models.CharField(max_length=2, choices=FLIGHT_CLASS)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    departure_date = models.DateTimeField()
    return_date = models.DateTimeField(blank=True)


class Ticket(models.Model):
    ticket_code = models.CharField(max_length=20)
    flight = models.OneToOneField(Flight, on_delete=models.CASCADE, related_name='tickets')


class User(models.Model):
    user = models.OneToOneField(User)
    profile_image = models.ImageField(upload_to="profile_images", blank=True)
    tickets = models.ManyToManyField(Ticket, blank=True)

