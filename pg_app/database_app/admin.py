from django.contrib import admin
from .models import Property

# Register your models here.
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('street_address', 'owner_name', 'number_associated_properties', 'list_associated_properties')

admin.site.register(Property, PropertyAdmin)