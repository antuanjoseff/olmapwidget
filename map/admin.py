from django.contrib import admin
from map.models import Zipcode
from django.contrib.gis.forms.widgets import OSMWidget

class ZipcodeAdmin(admin.ModelAdmin):
    pass

    
admin.site.register(Zipcode, ZipcodeAdmin)
# Register your models here.
