from timescale.db.models.fields import TimescaleDateTimeField
from timescale.db.models.managers import TimescaleManager
from django.db import models
# from django.contrib.gis.db.models import PointField

class Metric(models.Model):
    time = TimescaleDateTimeField(interval="1 day")
    # location = PointField()
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    objects = models.Manager()
    timescale = TimescaleManager()