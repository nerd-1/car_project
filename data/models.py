from django.db import models

class Cardata(models.Model):
    front_left = models.IntegerField()
    front_right = models.IntegerField()
    back_right = models.IntegerField()
    back_right = models.IntegerField()
    co = models.IntegerField()