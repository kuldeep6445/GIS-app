from django.contrib.gis.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=100)
    geom = models.PointField()

    def __str__(self) -> str:
        return self.name