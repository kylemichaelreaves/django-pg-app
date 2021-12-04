from django.contrib import admin
from .models import Property

# Register your models here.
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('property_id',
                    'street_address',
                    'owner_name',
                    'owner_mailing_address',
                    'city_state_zip',
                    'owner_full_mailing_address',
                    'property_full_address',
                    'units_at_property',
                    'g_code',
                    'latitude',
                    'longitude',
                    'number_associated_properties',
                    'list_associated_properties',
                    )

admin.site.register(Property, PropertyAdmin)
