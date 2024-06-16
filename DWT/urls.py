
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from rest_framework.routers import DefaultRouter
from testapp.views import SchulenViewSet, KindertageseinrichtungenViewSet, SchulsozialarbeitViewSet ,JugendberufshilfenViewSet


router = DefaultRouter()
router.register(r'schulen', SchulenViewSet)
router.register(r'kindertageseinrichtungen', KindertageseinrichtungenViewSet)
router.register(r'schulsozialarbeit', SchulsozialarbeitViewSet)
router.register(r'jugendberufshilfen', JugendberufshilfenViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('testing/', include("testapp.urls")),
    
    path('auth/', include('authapp.urls')),
    
    path('api/', include(router.urls)),

]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)