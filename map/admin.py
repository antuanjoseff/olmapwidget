from django.contrib import admin
from map.models import Zipcode


class ZipcodeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Zipcode, ZipcodeAdmin)
# Register your models here.
