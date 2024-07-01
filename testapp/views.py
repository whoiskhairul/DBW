from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize

import requests


from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model
from .serializers import JugendberufshilfenSerializer, KindertageseinrichtungenSerializer, SchulenGeoJSONSerializer, KindertageseinrichtungenGeoJSONSerializer, SchulenSerializer, SchulsozialarbeitGeoJSONSerializer, JugendberufshilfenGeoJSONSerializer, SchulsozialarbeitSerializer


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
    

    
            
    return JsonResponse({
        'message': 'Database updated successfully'
    })

def geojson(request):
    obj = Schulen.objects.all()
    # geo = serialize('geojson', obj, geometry_field='coordinates', fields=['kurzbezeichnung'])
    # return JsonResponse(geo, safe=False)
    # print('hello')
    
    return render(request, 'testing/geojson.html')


from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def facilitiesName(request):
    queryset1 = list(Schulen.objects.values_list('bezeichnung', flat=True))
    queryset2 = list(Kindertageseinrichtungen.objects.values_list('bezeichnung', flat=True))
    queryset3 = list(Schulsozialarbeit.objects.values_list('traeger', flat=True))
    queryset4 = list(Jugendberufshilfen.objects.values_list('traeger', flat=True))

    return Response({
        'Schulen': queryset1,
        'Kindertageseinrichtungen': queryset2,
        'Schulsozialarbeit': queryset3,
        'Jugendberufshilfen': queryset4,
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def add_to_favourite(request):
    # Accessing a query parameter named 'sourceId' and 'id'
    print(request.user)
    sourceId = request.GET.get('sourceId', '')
    id = request.GET.get('id', '')
    
    # Get the user
    User = get_user_model()
    user = User.objects.get(username=request.user.username)
    if sourceId == 'Schulen':
        s = Schulen.objects.get(id = int(id)).bezeichnung
    elif sourceId == 'Kindertageseinrichtungen':
        s = Kindertageseinrichtungen.objects.get(id = int(id)).bezeichnung
    if sourceId == 'Schulsozialarbeit':
        s = Schulsozialarbeit.objects.get(id = int(id)).traeger
    if sourceId == 'Jugendberufshilfen':
        s = Jugendberufshilfen.objects.get(id = int(id)).traeger

    # facility_name = sourceId.objects.get(id= id)
    print (sourceId, s)

    # Update the favourite_facility field
    user.favourite_facility = s
    user.save()

    return Response({
        'message': 'Favourite facility updated successfully'
    })



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def direction(request):
    # Accessing a query parameter named 'sourceId' and 'id'
    # print(request.user.username)
    User = get_user_model()
    user = User.objects.get(username=request.user.username)
    home = user.home_address
    
    fav = user.favourite_facility
    # fav = Jugendberufshilfen.objects.filter(traeger = fav)[0].coordinates
    latitude = ''
    longtude = ''
    try:
        latitude = Jugendberufshilfen.objects.filter(traeger = fav).first().latitude
        longtude = Jugendberufshilfen.objects.filter(traeger = fav).first().longitude
    except:
        pass
    try:
        latitude = Schulen.objects.filter(bezeichnung = fav).first().latitude
        longtude = Schulen.objects.filter(bezeichnung = fav).first().longitude
    except:
        pass
    try:
        latitude = Schulsozialarbeit.objects.filter(bezeichnung = fav).first().latitude
        longtude = Schulsozialarbeit.objects.filter(bezeichnung = fav).first().longitude
    except:
        pass
    try:
        latitude = Kindertageseinrichtungen.objects.filter(bezeichnung = fav).first().latitude
        longtude = Kindertageseinrichtungen.objects.filter(bezeichnung = fav).first().longitude
    except:
        pass
    latlong = str(longtude) + "," + str(latitude)
    print("latlong: ", latlong )
    # Get the user
    
    return Response({
        'source': home,
        'destination':latlong,
    })