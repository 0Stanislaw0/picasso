from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Crimes
from .serializers import CrimeSerializer



class CrimesFilter(filters.FilterSet):
    """ Filter crimes by report date"""
    date_from = filters.DateFilter(field_name='report_date', lookup_expr='gte')
    date_to = filters.DateFilter(field_name='report_date', lookup_expr='lte')


class CrimesList(generics.ListAPIView):
    """List crimes"""
    queryset = Crimes.objects.all()
    serializer_class = CrimeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CrimesFilter
    paginate_by = 20
