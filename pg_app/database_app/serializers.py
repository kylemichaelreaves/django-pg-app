from rest_framework import serializers
from .models import Property


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = (
            "property_id",
            "street_address",
            "owner_name",
            "owner_mailing_address",
            "city_state_zip",
            "owner_full_mailing_address",
            "property_full_address",
            "units_at_property",
            "g_code",
            "latitude",
            "longitude",
            "number_associated_properties",
            "list_associated_properties",
        )
