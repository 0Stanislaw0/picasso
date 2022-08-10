
from django.db import models


class Crimes(models.Model):
    crime_id = models.IntegerField(blank=True, null=True)
    original_crime_type_name = models.CharField(max_length=255,
                                                blank=True, null=True)
    report_date = models.DateField(blank=True, null=True)
    call_date = models.DateField(blank=True, null=True)
    offense_date = models.DateField(blank=True, null=True)
    call_time = models.TimeField(blank=True, null=True)
    call_date_time = models.DateTimeField(blank=True, null=True)
    disposition = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    agency_id = models.IntegerField(blank=True, null=True)
    address_type = models.CharField(max_length=255, blank=True, null=True)
    common_location = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.crime_id)

    class Meta:
        managed = False
        db_table = 'crimes'
