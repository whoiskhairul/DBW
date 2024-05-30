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
    path('update-data/', views.updateData, name='testing'),
    path('geojson/', views.geojson, name='geojson'),
    # path('api/', include(router.urls)),
]