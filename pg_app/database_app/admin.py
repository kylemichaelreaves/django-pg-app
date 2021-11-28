from django.contrib import admin
from .models import Property

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

# Register your models here.
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('street_address',
                    'owner_name',
                    'owner_mailing_address',
                    'city_state_zip',
                    'owner_full_mailing_address',
                    'property_full_address',
                    'units_at_property',
                    'number_associated_properties',
                    'list_associated_properties',
                    'g_code',
                    'latitude',
                    'longitude')

admin.site.register(Property, PropertyAdmin)
