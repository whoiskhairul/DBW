from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize

import requests

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import SchulenGeoJSONSerializer, KindertageseinrichtungenGeoJSONSerializer, SchulsozialarbeitGeoJSONSerializer, JugendberufshilfenGeoJSONSerializer


from testapp.models import Schulen, Kindertageseinrichtungen, Schulsozialarbeit, Jugendberufshilfen
# Create your views here.

# This section contains the  code for the API creation
class SchulenViewSet(viewsets.ModelViewSet):
    queryset = Schulen.objects.all()
    serializer_class = SchulenGeoJSONSerializer
    
class KindertageseinrichtungenViewSet(viewsets.ModelViewSet):
    queryset = Kindertageseinrichtungen.objects.all()
    serializer_class = KindertageseinrichtungenGeoJSONSerializer
    
class SchulsozialarbeitViewSet(viewsets.ModelViewSet):
    queryset = Schulsozialarbeit.objects.all()
    serializer_class = SchulsozialarbeitGeoJSONSerializer
    
class JugendberufshilfenViewSet(viewsets.ModelViewSet):
    queryset = Jugendberufshilfen.objects.all()
    serializer_class = JugendberufshilfenGeoJSONSerializer
    


def tesing(request):
    schule = serialize('geojson', Schulen.objects.all(), geometry_field='coordinates')

    kindertageseinrichtungen = serialize('geojson', Kindertageseinrichtungen.objects.all(), geometry_field='coordinates')

    schulsozialarbeit = serialize('geojson', Schulsozialarbeit.objects.all(), geometry_field='coordinates')

    jugendberufshilfen = serialize('geojson', Jugendberufshilfen.objects.all(), geometry_field='coordinates')

    context = {'schule': schule, 'kindertageseinrichtungen': kindertageseinrichtungen, 'schulsozialarbeit': schulsozialarbeit, 'jugendberufshilfen': jugendberufshilfen}
    
    
    return render(request, 'testing/index.html', context)

def updateData(request):

    req = requests.get("https://services6.arcgis.com/jiszdsDupTUO3fSM/arcgis/rest/services/Schulen_OpenData/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson")
    data = req.json()
    for feature in data['features']:
        properties = feature['properties']
        geometry = feature['geometry']
        try:
            Schulen.objects.create(
            id=properties['ID'],
            objectid=properties['OBJECTID'],
            typ=properties['TYP'],
            art=properties['ART'],
            standorttyp=properties['STANDORTTYP'],
            bezeichnung=properties['BEZEICHNUNG'],
            bezeichnungzusatz=properties.get('BEZEICHNUNGZUSATZ'),
            kurzbezeichnung=properties['KURZBEZEICHNUNG'],
            strasse=properties['STRASSE'],
            plz=properties['PLZ'],
            ort=properties['ORT'],
            telefon=properties['TELEFON'],
            fax=properties.get('FAX'),
            email=properties['EMAIL'],
            profile=properties.get('PROFILE'),
            sprachen=properties.get('SPRACHEN'),
            www=properties.get('WWW'),
            traeger=properties['TRAEGER'],
            traegertyp=properties['TRAEGERTYP'],
            bezugnr=properties['BEZUGNR'],
            gebietsartnummer=properties['GEBIETSARTNUMMER'],
            snummer=properties['SNUMMER'],
            nummer=properties['NUMMER'],
            globalid=properties['GlobalID'],
            creationdate=datetime.fromtimestamp(properties['CreationDate'] / 1000.0),
            creator=properties['Creator'],
            editdate=datetime.fromtimestamp(properties['EditDate'] / 1000.0),
            editor=properties['Editor'],
            latitude=geometry['coordinates'][1],
            longitude=geometry['coordinates'][0]
            )
        except Exception as e:
            print(e)
    

    req = requests.get("https://services6.arcgis.com/jiszdsDupTUO3fSM/arcgis/rest/services/Kindertageseinrichtungen_Sicht/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson")
    data = req.json()
    for feature in data['features']:
        properties = feature['properties']
        geometry = feature['geometry']
        try:
            Kindertageseinrichtungen.objects.create(
            id=properties['ID'],
            objectid=properties['OBJECTID'],
            traeger=properties['TRAEGER'],
            bezeichnung=properties['BEZEICHNUNG'],
            kurzbezeichnung=properties['KURZBEZEICHNUNG'],
            strasse=properties['STRASSE'],
            strschl=properties.get('STRSCHL'),
            hausbez=properties['HAUSBEZ'],
            plz=properties['PLZ'],
            ort=properties['ORT'],
            hort=properties['HORT'],
            kita=properties['KITA'],
            url=properties.get('URL'),
            telefon=properties['TELEFON'],
            fax=properties.get('FAX'),
            email=properties.get('EMAIL'),
            barrierefrei=properties.get('BARRIEREFREI'),
            integrativ=properties['INTEGRATIV'],
            latitude=geometry['coordinates'][1],
            longitude=geometry['coordinates'][0]
            )
        except Exception as e:
            print(e)
            print(properties.get('OBJECTID'))
    

    req = requests.get("https://services6.arcgis.com/jiszdsDupTUO3fSM/arcgis/rest/services/Schulsozialarbeit_FL_1/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson")
    data = req.json()
    for feature in data['features']:
        properties = feature['properties']
        geometry = feature['geometry']
        try:
            Schulsozialarbeit.objects.create(
            id=properties['ID'],
            objectid=properties['OBJECTID'],
            traeger=properties['TRAEGER'],
            leistungen=properties['LEISTUNGEN'],
            bezeichnung=properties['BEZEICHNUNG'],
            kurzbezeichnung=properties['KURZBEZEICHNUNG'],
            strasse=properties['STRASSE'],
            plz=properties['PLZ'],
            ort=properties['ORT'],
            telefon=properties['TELEFON'],
            email=properties.get('EMAIL'),
            fax=properties.get('FAX'),
            latitude=geometry['coordinates'][1],
            longitude=geometry['coordinates'][0]
            )
        except Exception as e:
            print(e)
            print(properties.get('OBJECTID'))


    req = requests.get("https://services6.arcgis.com/jiszdsDupTUO3fSM/arcgis/rest/services/Jugendberufshilfen_FL_1/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson")
    data = req.json()
    for feature in data['features']:
        properties = feature['properties']
        geometry = feature['geometry']
        try:
            Jugendberufshilfen.objects.create(
            id=properties['ID'],
            objectid=properties['OBJECTID'],
            traeger=properties['TRAEGER'],
            leistungen=properties['LEISTUNGEN'],
            bezeichnung=properties['BEZEICHNUNG'],
            kurzbezeichnung=properties['KURZBEZEICHNUNG'],
            strasse=properties['STRASSE'],
            plz=properties['PLZ'],
            ort=properties['ORT'],
            telefon=properties['TELEFON'],
            email=properties.get('EMAIL'),
            fax=properties.get('FAX'),
            latitude=geometry['coordinates'][1],
            longitude=geometry['coordinates'][0]
            )
        except Exception as e:
            print(e)
            print(properties.get('OBJECTID'))
    

    
            
    return render(request, 'testing/static.html')

def geojson(request):
    obj = Schulen.objects.all()
    # geo = serialize('geojson', obj, geometry_field='coordinates', fields=['kurzbezeichnung'])
    # return JsonResponse(geo, safe=False)
    # print('hello')
    
    return render(request, 'testing/geojson.html')
