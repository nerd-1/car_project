from rest_framework import serializers
from . import models

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cardata
        fields = '__all__'
