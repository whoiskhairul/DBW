from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Schulen, Kindertageseinrichtungen, Schulsozialarbeit, Jugendberufshilfen


class SchulenGeoJSONSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Schulen
        geo_field = 'coordinates'
        fields = '__all__'

class KindertageseinrichtungenGeoJSONSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Kindertageseinrichtungen
        geo_field = 'coordinates'
        fields = '__all__'

class SchulsozialarbeitGeoJSONSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Schulsozialarbeit
        geo_field = 'coordinates'
        fields = '__all__'

class JugendberufshilfenGeoJSONSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Jugendberufshilfen
        geo_field = 'coordinates'
        fields = '__all__'



class SchulenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schulen
        fields = 'bezeichnung'

class KindertageseinrichtungenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kindertageseinrichtungen
        fields = 'bezeichnung'

class SchulsozialarbeitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schulsozialarbeit
        fields = 'bezeichnung'

class JugendberufshilfenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugendberufshilfen
        fields = 'bezeichnung'


