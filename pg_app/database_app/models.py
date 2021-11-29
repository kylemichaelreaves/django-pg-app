from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Property(models.Model):
    street_address = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    owner_mailing_address = models.CharField(max_length=255)
    city_state_zip = models.CharField(max_length=255)
    property_full_address = models.CharField(max_length=255)
    owner_full_mailing_address = models.CharField(max_length=255)
    units_at_property = models.IntegerField()
    g_code = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    number_associated_properties = models.IntegerField()
    list_associated_properties = ArrayField(models.CharField(max_length=255))

class Landlord(models.Model):
    name = models.CharField(max_length=255)
    mailing_address = models.CharField(max_length=255)
    city_state_zip = models.CharField(max_length=255)
    full_mailing_address = models.CharField(max_length=255)
    number_properties_owned = models.IntegerField()
    list_properties_owned = ArrayField(models.CharField(max_length=255))
