from django.urls import path
from .api_views import CrimesList


urlpatterns = [
    path('crimes/', CrimesList.as_view(), name='crimes'),
    ]
