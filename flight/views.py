from rest_framework.decorators import api_view
# from rest_framework.response import Response
from django.http import JsonResponse,HttpResponse
from django.contrib.auth import authenticate, login
from .serializers import *
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout


@api_view(['POST'])
@csrf_exempt
def login_user(request):
    """
    verifies user email and password and returns user's token.
    """
    # data = {}
    reqBody = request.POST
    user_email = reqBody.get('email')
    password = reqBody.get('password')
    user = User.objects.get(email=user_email)
    user = authenticate(username=user.username, password=password)
    if user is not None:
        print(user.username)
        user_token = Token.objects.get(user=user)
        user_token = user_token.key
        print(user_token)

        response = {"user_email": user_email, 'token': user_token}
        return JsonResponse(response)
    else:
        print("wow")
        return JsonResponse({"message": "message does not exist"})



@api_view(['POST'])
@csrf_exempt
def signup_user(request):
    """
    verifies user email and password and returns user's token.
    """
    # data = {}
    reqBody = request.POST
    username = reqBody.get("name")
    user_email = reqBody.get('email')
    user_password = reqBody.get('password')
    if user_email and user_password:
        # check if user exists
        user = User.objects.get(email = user_email)
        if user is None:
            user = User.objects.create_user(username=username, email=user_email, password=user_password)
            user.save()         # A token for the user is automatically generated once the user is first created
            user_token = Token.objects.get(user=user)
            user_token = user_token.key

            response = {"user_email": user_email, 'token': user_token, 'message': "Account creation successful."}
            return JsonResponse(response)
        else:
            return JsonResponse({"message": "Email is already associated with an account."})
    else: return JsonResponse({'message': "email and password are required."})


@api_view(['GET',])
@permission_classes((IsAuthenticated, ))
def flights(request):
    """
    :returns: a list of flights available
    """
    print(request.user)
    all_flights = Flight.objects.all()
    flights_serializer = FlightSerializer(all_flights, many=True)
    return JsonResponse(flights_serializer.data, safe=False)


@api_view(['GET',])
@permission_classes((IsAuthenticated, ))
def get_user_profile(request):
    response = {}
    user  = request.user
    user_info = User.objects.filter(user=user)
    #print(user_info)
    response['user_info'] = user_info
    return response

@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def logout(request):
    request.user.auth_token.delete()
    logout(request)


@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def book_flight(request):
    """
    ......./book_flight?flight_id=2&payment_status="successful"
    """
    flight_id = request.GET['flight_id']
    payment_status = request.GET['payment_status']
    if payment_status == "successful":
        flight = Flight.objects.get(id=flight_id)
        user = request.user
        ticket = Ticket(user=user, flight=flight)
        ticket.save()
        print(user.tickets.all())
        response = {"status": "successful", "data":{"ticket_code": ticket.ticket_code}}
        return JsonResponse(response)
    else:
        response = {"status": "error", "data": {"error_code": "payment required"}}
        return JsonResponse(response)


@api_view(['GET', ])
def list_cities(request):
    all_cities = City.objects.all()
    city_serializer = CitySerializer(all_cities, many=True)
    return JsonResponse(city_serializer.data, safe=False)


