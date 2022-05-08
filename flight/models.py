from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# creates a unique auth token when a user is created
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class City(models.Model):
    country_name = models.CharField(max_length=100)
    city_code = models.CharField(max_length=5)
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city_name}"


class Airport(models.Model):
    name = models.CharField(max_length=100)
    city_code = models.ForeignKey(City, on_delete=models.RESTRICT)
    terminal = models.CharField(max_length=50)
    gate = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Airplane(models.Model):
    name = models.CharField(max_length=50)
    number_of_seats = models.IntegerField()

    def __str__(self):
        return f"{self.name}"


class Flight(models.Model):
    FLIGHT_TYPES = [('OW', 'One Way'), ('RT', 'Round Trip')]
    FLIGHT_CLASS = [('FC', 'First Class'), ('BC', 'Business Class'), ('E', 'Economy')]
    airplane = models.ForeignKey(Airplane, on_delete=models.RESTRICT, related_name="flights")
    source = models.ForeignKey(City, on_delete=models.RESTRICT, related_name="moving_flights")
    destination = models.ForeignKey(City, on_delete=models.RESTRICT, related_name="arriving_flights")
    duration = models.DecimalField(decimal_places=2, max_digits=10)
    flight_type = models.CharField(max_length=2, choices=FLIGHT_TYPES)
    flight_class = models.CharField(max_length=2, choices=FLIGHT_CLASS)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    departure_date = models.DateTimeField()
    return_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.source} to {self.destination}"


def rand_code():
    import random
    tickets = Ticket.objects.all()
    codes = [ticket.ticket_code for ticket in tickets]
    t = True
    while t:
        r = random.randint(100, 999)
        if f"DH{r}" not in codes:
            t = False
    return f"DH{r}"


class Ticket(models.Model):
    ticket_code = models.CharField(max_length=20, unique=True, default=rand_code)
    user = models.ForeignKey(User, related_name='tickets', on_delete=models.RESTRICT, null=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='tickets')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="profile_images", blank=True)
