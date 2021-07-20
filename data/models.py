from django.db import models

class Cardata(models.Model):
    car_id = models.BigAutoField(primary_key=True)
    front_left = models.IntegerField()
    front_right = models.IntegerField()
    back_left = models.IntegerField()
    back_right = models.IntegerField()
    co = models.IntegerField()

class CardataRecord(models.Model):
    record_id = models.BigAutoField(primary_key=True)
    car_id = models.IntegerField()
    front_left = models.IntegerField()
    front_right = models.IntegerField()
    back_left = models.IntegerField()
    back_right = models.IntegerField()
    co = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)