from rest_framework import serializers
from .models import Crimes


class CrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crimes
        fields = '__all__'
