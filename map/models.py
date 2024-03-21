from django.contrib.gis.db import models
# from django.db import models

class Zipcode(models.Model):
    code = models.CharField(max_length=5)
    poly = models.MultiPolygonField()

    def __str__(self):
        return f"{self.code}"