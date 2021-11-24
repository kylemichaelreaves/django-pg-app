from django.db import models
from django.contrib.postgres.fields import ArrayField

"""
    street_address
    owner_name
    owner_mailing_address
    city_state_zip
    owner_full_mailing_address
    property_full_address
    units_at_property
    number_properties_owned
    list_properties_owned
    g_code
    latitude
    longitude
"""

class Property(models.Model):
    street_address = models.CharField()
    owner_name = models.CharField()
    owner_mailing_address = models.CharField()
    city_state_zip = models.CharField()
    owner_full_mailing_address = models.CharField()
    property_full_address = models.CharField()
    units_at_property = models.IntegerField()
    number_properties_owned = models.IntegerField()
    list_properties_owned = ArrayField(models.CharField())
    g_code = models.CharField()
    latitude = models.FloatField()
    longitude = models.FloatField()

class Landlord(models.Model):
    name = models.CharField()
    mailing_address = models.CharField()
    city_state_zip = models.CharField()
    full_mailing_address = models.CharField()
    list_properties_owned = ArrayField(models.CharField())
    number_properties_owned = models.IntegerField()

