from django.urls import path
from rest_framework.authtoken import views as auth_views
from . import views

urlpatterns = [


    # api endpoint for obtaining authentication token for a user
    path("api-token-auth/", auth_views.obtain_auth_token),
]