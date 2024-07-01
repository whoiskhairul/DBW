from django.urls import path, include


# from rest_framework.routers import DefaultRouter
# from .views import SchulenViewSet, KindertageseinrichtungenViewSet, SchulsozialarbeitViewSet ,JugendberufshilfenViewSet

from . import views


# router = DefaultRouter()
# router.register(r'schulen', SchulenViewSet)
# router.register(r'kindertageseinrichtungen', KindertageseinrichtungenViewSet)
# router.register(r'schulsozialarbeit', SchulsozialarbeitViewSet)
# router.register(r'jugendberufshilfen', JugendberufshilfenViewSet)


urlpatterns = [
    path('', views.tesing, name='testing'),
    path('geojson/', views.geojson, name='geojson'),
    path('facilities/', views.facilitiesName, name='fac'),
    path('add-to-favourite/', views.add_to_favourite, name='favourite'),
    path('direction/', views.direction, name='direction'),
    path('update-data/', views.updateData, name='up'),
    
    # path('api/', include(router.urls)),
]