from django.db import models
from django.contrib.gis.db.models import PointField
from django.contrib.gis.geos import Point

# Create your models here.

class Schulen(models.Model):
    id = models.AutoField(primary_key=True)
    objectid = models.IntegerField(null=True, unique=False)
    typ = models.IntegerField(null=True, blank=True)
    art = models.CharField(max_length=255, null=True, blank=True)
    standorttyp = models.CharField(max_length=255, null=True, blank=True)
    bezeichnung = models.CharField(max_length=255, null=True, blank=True)
    bezeichnungzusatz = models.TextField(null=True, blank=True)
    kurzbezeichnung = models.CharField(max_length=255, null=True, blank=True)
    strasse = models.CharField(max_length=255, null=True, blank=True)
    plz = models.CharField(max_length=10, null=True, blank=True)
    ort = models.CharField(max_length=255, null=True, blank=True)
    telefon = models.CharField(max_length=20, null=True, blank=True)
    fax = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    profile = models.TextField(null=True, blank=True)
    sprachen = models.TextField(null=True, blank=True)
    www = models.URLField(null=True, blank=True)
    traeger = models.CharField(max_length=255, null=True, blank=True)
    traegertyp = models.IntegerField(null=True, blank=True)
    bezugnr = models.CharField(null=True, blank=True, max_length=255)
    gebietsartnummer = models.IntegerField(null=True, blank=True)
    snummer = models.IntegerField(null=True, blank=True)
    nummer = models.IntegerField(null=True, blank=True)
    globalid = models.CharField(max_length=255, null=True, blank=True)
    creationdate = models.DateTimeField()
    creator = models.CharField(max_length=255)
    editdate = models.DateTimeField()
    editor = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    coordinates = PointField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.coordinates = Point(self.longitude, self.latitude)
        super(Schulen, self).save(*args, **kwargs)  # Call the real save() method

    def __str__(self):
        return self.kurzbezeichnung


class Kindertageseinrichtungen(models.Model):
    id = models.AutoField(primary_key=True)
    objectid = models.IntegerField(null=True, unique=False)
    traeger = models.CharField(max_length=255)
    bezeichnung = models.CharField(max_length=255)
    kurzbezeichnung = models.CharField(max_length=255)
    strasse = models.CharField(max_length=255)
    strschl = models.CharField(max_length=10)
    hausbez = models.CharField(max_length=10)
    plz = models.CharField(max_length=10)
    ort = models.CharField(max_length=255)
    hort = models.CharField(max_length=255)
    kita = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)
    telefon = models.CharField(max_length=50)
    fax = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    barrierefrei = models.CharField(max_length=255)
    integrativ = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    coordinates = PointField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.coordinates = Point(self.longitude, self.latitude)
        super(Kindertageseinrichtungen, self).save(*args, **kwargs)  # Call the real save() method

    def __str__(self):
        return self.kurzbezeichnung


class Schulsozialarbeit(models.Model):
    id = models.AutoField(primary_key=True)
    objectid = models.IntegerField(null=True, unique=False)
    traeger = models.CharField(max_length=255)
    leistungen = models.CharField(max_length=255)
    bezeichnung = models.CharField(max_length=255, null=True, blank=True)
    kurzbezeichnung = models.CharField(max_length=255, null=True, blank=True)
    strasse = models.CharField(max_length=255)
    plz = models.CharField(max_length=10)
    ort = models.CharField(max_length=255)
    telefon = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    fax = models.CharField(max_length=20, null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    coordinates = PointField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.coordinates = Point(self.longitude, self.latitude)
        super(Schulsozialarbeit, self).save(*args, **kwargs)  # Call the real save() method

    def __str__(self):
        return self.traeger


class Jugendberufshilfen(models.Model):
    id = models.AutoField(primary_key=True)
    objectid = models.IntegerField(null=True, unique=False)
    traeger = models.CharField(max_length=255)
    leistungen = models.CharField(max_length=255)
    bezeichnung = models.CharField(max_length=255, null=True, blank=True)
    kurzbezeichnung = models.CharField(max_length=255, null=True, blank=True)
    strasse = models.CharField(max_length=255)
    plz = models.CharField(max_length=10)
    ort = models.CharField(max_length=255)
    telefon = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    fax = models.CharField(max_length=20, null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    coordinates = PointField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.coordinates = Point(self.longitude, self.latitude)
        super(Jugendberufshilfen, self).save(*args, **kwargs)  # Call the real save() method

    def __str__(self):
        return self.traeger