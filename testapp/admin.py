from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin

from .models import Schulen, Kindertageseinrichtungen, Schulsozialarbeit, Jugendberufshilfen
# Register your models here.

class CustomZoomAdmin(GISModelAdmin):
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 11,
        },
    }

admin.site.register(Schulen, CustomZoomAdmin)
admin.site.register(Kindertageseinrichtungen)
admin.site.register(Schulsozialarbeit)
admin.site.register(Jugendberufshilfen)
