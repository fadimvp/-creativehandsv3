from django.db import models


# Create your models here.


class Brand(models.Model):
    PRAName = models.CharField(max_length=120)
    PRADesc = models.TextField()

    def __str__(self):
        return self.PRAName


class Variant(models.Model):
    VARName = models.CharField(max_length=120)
    VARDesc = models.TextField()

    def __str__(self):
        return self.VARName
