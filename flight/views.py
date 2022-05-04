from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from .models import *
from .serializers import *
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout



# Create your views here.
@api_view(['POST'])
def login_user(request):
    data = {}
    reqBody = JsonResponse.loads(request.body)
    user_email = reqBody['Email_Address']
    user_password = reqBody['password']
    user = authenticate(request, )
    token = Token.objects.get_or_create(user=Account)[0].key
    if not check_password(password, Account.password):
        raise ValidationError({"message": "Incorrect Login"})

    if Account:
        if Account.is_active:
            print(request.user)
            login(request, Account)
            data["message"] = "user logged in"
            data["email_address"] = Account.email

            response = {"data": data, "token": token}

            return Response(Res)

        else:
            raise ValidationError({"400": f'Account not active'})

    else:
        raise ValidationError({"400": f'Account doesnt exist'})

@api_view(['GET',])
@permission_classes((IsAuthenticated, ))
def flights(request):
    all_flights = Flight.objects.all()
    flights_serializer = FlightSerializer(all_flights, many=True)
    return JsonResponse(flights_serializer.data, safe=False)
      
@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def logout(request):
    request.user.auth_token.delete()
    logout(request)
    #redirect should be added after this line @janprince

