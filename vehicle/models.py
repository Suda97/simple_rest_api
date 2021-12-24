from django.db import models


# Create your models here.
# Simple table model for simple rest api!
class Vehicle(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    avg_rating = models.FloatField()
    rates_number = models.BigIntegerField()

    def __str__(self):
        return self.model